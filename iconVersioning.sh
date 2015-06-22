#!/bin/sh
export PATH=/opt/local/bin/:/opt/local/sbin:$PATH:/usr/local/bin:

#Adding Environment key to info.plist if already not there
if ! grep -q "<key>Environment</key>" "${INFOPLIST_FILE}"; then
sed -i '' 's/<key>CFBundleIdentifier<\/key>/<key>Environment<\/key><string>Live<\/string><key>CFBundleIdentifier<\/key>/' "${INFOPLIST_FILE}"
else
echo "key already exists"
fi

convertPath=`which convert`
echo ${convertPath}
if [[ ! -f ${convertPath} || -z ${convertPath} ]]; then
  echo "WARNING: Skipping Icon versioning, you need to install ImageMagick and ghostscript (fonts) first, you can use brew to simplify process:
  brew install imagemagick
  brew install ghostscript"
exit 0;
fi

version=`/usr/libexec/PlistBuddy -c "Print CFBundleShortVersionString" "${INFOPLIST_FILE}"`
environment=`/usr/libexec/PlistBuddy -c "Print Environment" "${INFOPLIST_FILE}"`

#SRCROOT=..
#CONFIGURATION_BUILD_DIR=.
#UNLOCALIZED_RESOURCES_FOLDER_PATH=.

shopt -s extglob
#build_num="${build_num##*( )}"
shopt -u extglob
caption="Ver: ${version} \nServer: ${environment}"
echo $caption

function abspath() { pushd . > /dev/null; if [ -d "$1" ]; then cd "$1"; dirs -l +0; else cd "`dirname \"$1\"`"; cur_dir=`dirs -l +0`; if [ "$cur_dir" == "/" ]; then echo "$cur_dir`basename \"$1\"`"; else echo "$cur_dir/`basename \"$1\"`"; fi; fi; popd > /dev/null; }

function processIcon() {
    base_file=$1
    
    cd "${CONFIGURATION_BUILD_DIR}/${UNLOCALIZED_RESOURCES_FOLDER_PATH}"
    base_path=`find . -name ${base_file}`
    
    real_path=$( abspath "${base_path}" )
    echo "base path ${real_path}"
    
    if [[ ! -f ${base_path} || -z ${base_path} ]]; then
      return;
    fi
    
    # TODO: if they are the same we need to fix it by introducing temp
    target_file=`basename $base_path`
    target_path="${CONFIGURATION_BUILD_DIR}/${UNLOCALIZED_RESOURCES_FOLDER_PATH}/${target_file}"
    
    base_tmp_normalizedFileName="${base_file%.*}-normalized.${base_file##*.}"
    base_tmp_path=`dirname $base_path`
    base_tmp_normalizedFilePath="${base_tmp_path}/${base_tmp_normalizedFileName}"
    
    stored_original_file="${base_tmp_normalizedFilePath}-tmp"
    if [[ -f ${stored_original_file} ]]; then
      echo "found previous file at path ${stored_original_file}, using it as base"
      mv "${stored_original_file}" "${base_path}"
    fi

    shopt -s nocasematch
    if [[ $environment = "Live" ]]; then
        cp "${base_path}" "$target_path"
        return 0;
    fi
    shopt -u nocasematch

    if [ ! "$environment" ];then
        echo "ERROR: Operation not allowed. This build is not pointing to Live Server. Please change the server configuration from info.plist -> Environment"
        exit 1;
    fi

    shopt -s nocasematch
    if [[ $CONFIGURATION = "Release" ]]; then
        if [[ $environment != "Live" ]]; then
            echo "ERROR: Operation not allowed. This build is not pointing to Live Server. Please change the server configuration from info.plist -> Environment"
            exit 1;
        fi
    fi
    shopt -u nocasematch

    echo "Reverting optimized PNG to normal"
    # Normalize
    echo "xcrun -sdk iphoneos pngcrush -revert-iphone-optimizations -q ${base_path} ${base_tmp_normalizedFilePath}"
    xcrun -sdk iphoneos pngcrush -revert-iphone-optimizations -q "${base_path}" "${base_tmp_normalizedFilePath}"
    
    # move original pngcrush png to tmp file
    echo "moving pngcrushed png file at ${base_path} to ${stored_original_file}"
    #rm "$base_path"
    mv "$base_path" "${stored_original_file}"
    
    # Rename normalized png's filename to original one
    echo "Moving normalized png file to original one ${base_tmp_normalizedFilePath} to ${base_path}"
    mv "${base_tmp_normalizedFilePath}" "${base_path}"
    
    width=`identify -format %w ${base_path}`
    height=`identify -format %h ${base_path}`
    band_height=$((($height * 35) / 100))
    band_position=$(($height - $band_height - 10))
    text_position=$(($band_position - 3))
    point_size=$(((13 * $width) / 100))
    
    echo "Image dimensions ($width x $height) - band height $band_height @ $band_position - point size $point_size"
    
    #
    # blur band and text
    #
    convert ${base_path} -blur 10x8 /tmp/blurred.png
    convert /tmp/blurred.png -gamma 0 -fill white -draw "rectangle 0,$band_position,$width,$height" /tmp/mask.png
    convert -size ${width}x${band_height} xc:none -fill 'rgba(1,1,1,0.7)' -draw "rectangle 0,0,$width,$band_height" /tmp/labels-base.png
    convert -background none -size ${width}x${band_height} -pointsize $point_size -fill white -gravity center -gravity South caption:"$caption" /tmp/labels.png
    
    convert ${base_path} /tmp/blurred.png /tmp/mask.png -composite /tmp/temp.png
    
    rm /tmp/blurred.png
    rm /tmp/mask.png
    
    #
    # compose final image
    #
    filename=New${base_file}
    convert /tmp/temp.png /tmp/labels-base.png -geometry +0+$band_position -composite /tmp/labels.png -geometry +0+$text_position -geometry +${w}-${h} -composite "${target_path}"
    
    # clean up
    rm /tmp/temp.png
    rm /tmp/labels-base.png
    rm /tmp/labels.png
    
    echo "Overlayed ${target_path}"
}

icon_count=`/usr/libexec/PlistBuddy -c "Print CFBundleIcons:CFBundlePrimaryIcon:CFBundleIconFiles" "${CONFIGURATION_BUILD_DIR}/${INFOPLIST_PATH}" | wc -l`
last_icon_index=$((${icon_count} - 2))

i=0
while [  $i -lt $last_icon_index ]; do
  icon=`/usr/libexec/PlistBuddy -c "Print CFBundleIcons:CFBundlePrimaryIcon:CFBundleIconFiles:$i" "${CONFIGURATION_BUILD_DIR}/${INFOPLIST_PATH}"`

  if [[ $icon == *.png ]] || [[ $icon == *.PNG ]]
  then
    processIcon $icon
  else
    processIcon "${icon}.png"
    processIcon "${icon}@2x.png"
    processIcon "${icon}@3x.png"
  fi
  let i=i+1
done

# Workaround to fix issue#16 to use wildcard * to actually find the file
# Only 72x72 and 76x76 that we need for ipad app icons
processIcon "AppIcon72x72~ipad*"
processIcon "AppIcon72x72@2x~ipad*"
processIcon "AppIcon76x76~ipad*"
processIcon "AppIcon76x76@2x~ipad*"