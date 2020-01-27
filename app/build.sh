
rm -rf www
mkdir wwww
cp ../index.html www
cp -r ../css www
cp -r ../data www
cp -r ../js www
cp -r ../assets www

export ANDROID_HOME=/home/niyasc/Development
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-amd64
export PATH=$PATH:/home/niyasc/.gradle/wrapper/dists/gradle-4.1-all/bzyivzo6n839fup2jbap0tjew/gradle-4.1/bin
export PATH=$PATH:/home/niyasc/Development/tools
export PATH=$PATH:/home/niyasc/Development/platform-tools
trap interrupted INT
function interrupted () {
    rm -f platforms/android/release.properties
}

# stty -echo
# read -p "Store Password: " spassw; echo
# read -p "Key Password: " kpassw; echo
# stty echo

cat << EOT > platforms/android/release.properties
storeFile=../../malayalamlive.keystore
storePassword=malayalamlive
keyAlias=release_key
keyPassword=malayalamlive
EOT

export ORG_GRADLE_PROJECT_cdvReleaseSigningPropertiesFile=../release.properties 
cordova build --release android
rm platforms/android/release.properties

echo "Build completed, trying to kill java daeomon"
pkill java
