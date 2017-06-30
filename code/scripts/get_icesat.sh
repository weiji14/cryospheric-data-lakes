#Bash script based off https://nsidc.org/support/faq/what-options-are-available-bulk-downloading-data-https-earthdata-login-enabled WGET Instructions - for command line in Mac and Unix/Linux
#
#generate .netrc file from interactive prompt
touch ~/.netrc  #note that this file will have to exist in your linux home directory
read -p "Eartdata login username: " user
read -s -p "Eartdata login password: " pass
echo "machine urs.earthdata.nasa.gov login $user password $pass" >> ~/.netrc
chmod 0600 ~/.netrc

#create cookies file
touch .urs_cookies
#trigger authentication first
wget -c -P ../data/icesat --load-cookies .urs_cookies --save-cookies .urs_cookies --keep-session-cookies --no-check-certificate --auth-no-challenge=on -r --reject "index.html*,icons" -nH -np --cut-dirs=1 -e robots=off "https://n5eil01u.ecs.nsidc.org/GLAS/GLA12.034/"
#does actual download
wget -c -P ../data/icesat --load-cookies .urs_cookies --save-cookies .urs_cookies --keep-session-cookies --no-check-certificate --auth-no-challenge=on -r --reject "index.html*,icons" -nH -np --cut-dirs=1 --tries=5 -e robots=off "https://n5eil01u.ecs.nsidc.org/GLAS/GLA12.034/"

#final tidy up
rm .urs_cookies
sed -i '$d' ~/.netrc
