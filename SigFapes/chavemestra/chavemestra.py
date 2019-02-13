#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(args):
	#shp_do_raster()
	#gdal_warp()
	#dowload_ecw()
	#recorte("V:\Vinicius\recorte\COSTA\XXX.shp ","b\XXX.tif ","c/XXX.tif ")
	return 0
	
def dowload_ecw():
	arq = open("contorno.txt","rt")
	arqout = open("comandos.txt","wt")
	
	pref = "http://www2.geobases.es.gov.br/ftppublico/MapES_2012-2015/IMG_ECW/XXX.ecw\n"
	linha = arq.readline(marc, linha[:-1])
	
	while (linha != ""):
		pref = pref.replace(marc, linha[:-1])
		arqout.write(comp)
		linha = arq.readline()
		comp = ""
		
	arq.close()
	arqout.close()	
	return 0

def shp_do_raster():
	arq = open("contorno.txt","rt")
	arqout = open("comandos.txt","wt")
	marc = "XXX"
	pref = 'gdaltindex -tileindex location -f "ESRI Shapefile" C:/Users/Vinicius/Desktop/SIGWEB/shp/XXX.shp C:/Users/Vinicius/Desktop/SIGWEB/tif/XXX.tif\n'

	linha = arq.readline()
	
	while (linha != ""):
		pref = pref.replace(marc,linha[:-1])
		arqout.write(pref)
		linha = arq.readline()
		pref = 'gdaltindex -tileindex location -f "ESRI Shapefile" C:/Users/Vinicius/Desktop/SIGWEB/shp/XXX.shp C:/Users/Vinicius/Desktop/SIGWEB/tif/XXX.tif\n'
		
	arq.close()
	arqout.close()
	return 0

def gdal_warp():
	arq = open("contorno.txt","rt")
	arqout = open("comandos.txt","wt")
	marc = "XXX"
	
	pref = "gdalwarp -s_srs EPSG:31984 -multi -of GTiff C:/Users/Vinicius/Desktop/SIGWEB/ecw/XXX.ecw C:/Users/Vinicius/Desktop/SIGWEB/tif/XXX.tif\n"
	linha = arq.readline()
	
	while (linha != ""):
		pref = pref.replace(marc,linha[:-1])
		arqout.write(pref)
		linha = arq.readline()
		pref = "gdalwarp -s_srs EPSG:31984 -multi -of GTiff C:/Users/Vinicius/Desktop/SIGWEB/ecw/XXX.ecw C:/Users/Vinicius/Desktop/SIGWEB/tif/XXX.tif\n"
		
	arq.close()
	arqout.close()
	return 0

def recorte(Dshp, DtifI, DtifO):
	arq = open("conflito.costa.txt","rt")
	arqout = open("comandos.txt","wt")

	pref = "gdalwarp -multi -cutline " + Dshp + DtifI + DtifO +"\n"
	marc = "XXX"
	linha = arq.readline()
	
	while (linha != ""):
		pref = pref.replace(marc,linha[:-1])
		arqout.write(pref)
		linha = arq.readline()
		pref = "gdalwarp -multi -cutline " + Dshp + DtifI + DtifO +"\n"

	arq.close()
	arqout.close()
	return 0
	
def corversao(DirO, Dir1):
	arq = open("conflito.costa.txt","rt")
	arqout = open("corvesao.txt","wt")
	
	pref = "gdal_translate -of GTiff -ot UInt16 Dir0 Dir1 -co COMPRESS=LZW -co PREDICTOR=2 -co bigtiff=yes -co tfw=yes\n"
	pref = pref.replace("Dir0", Dir0)
	pref = pref.replace("Dir1", Dir1)
	base = pref
	marc = "XXX"
	linha = arq.readline()

	while (linha != ""):
		out = base.replace(marc,linha[:-1])
		arqout.write(out)
		linha = arq.readline()

	arq.close()
	arqout.close()
	return 0

def projecao(Dir0, Dir1):
	arq = open("conflito.costa.txt","rt")
	arqout = open("projecao.txt","wt")
	
	pref = "gdalwarp -multi -overwrite -t_srs EPSG:31984 Dir0 Dir1\n"
	pref = pref.replace("Dir0", Dir0)
	pref = pref.replace("Dir1", Dir1)
	base = pref
	marc = "XXX"
	linha = arq.readline()
	
	while (linha != ""):
		out = base.replace(marc,linha[:-1])
		arqout.write(out)
		linha = arq.readline()

	arq.close()
	arqout.close()
	return 0

def compressao(Dir0, Dir1):
	arq = open("conflito.costa.txt","rt")
	arqout = open("compressao.txt","wt")
	
	pref = "gdal_translate -of GTiff -ot UInt16 Dir0 Dir1 -co COMPRESS=DEFLATE -co PREDICTOR=2 -co bigtiff=yes -co tfw=yes\n"
	pref = pref.replace("Dir0", Dir0)
	pref = pref.replace("Dir1", Dir1)
	base = pref
	marc = "XXX"
	linha = arq.readline()
	
	while (linha != ""):
		out = base.replace(marc,linha[:-1])
		arqout.write(out)
		linha = arq.readline()

	arq.close()
	arqout.close()
	return 0
	
if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
