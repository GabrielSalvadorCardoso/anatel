# anatel
anatel uses python3 and pip

## intall project python dependencies
pip install -r requirements.txt

## anatel uses mapnik, to install it
https://github.com/mapnik/mapnik/wiki/UbuntuInstallation

## in the case of errors involving the C++ compiler
https://github.com/mapnik/mapnik/issues/3769

## install mapnik python bidings
pip3 install mapnik

## if the previous command doesn't work
https://github.com/mapnik/python-mapnik

anatel uses PostgreSQL with spatial extansion PostGIS. Feel free to use whatever database with spatial extansion you want

## anatel spatial data (Brazil - .shp.zip)
http://sistemas.anatel.gov.br/geoserver/ANATEL/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=vw_tvd&outputFormat=SHAPE-ZIP

## using shp2pgsql to transfer shapefiles to postgres/postgis
https://www.bostongis.com/pgsql2shp_shp2pgsql_quickguide.bqg
