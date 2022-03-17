#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import os



def numfill(value):
    return str(value).zfill(2)

def  template_remove_map(template):
    txt = '''
    
    <!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<!-- mapnik -->
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" integrity="sha512-xodZBNTC5n17Xt2atTPuE1HxjVMSvLVW9ocqUKLsCC5CXdbqCmblAshOMAS6/keqq/sMZMZ19scR4PsZChSR7A==" crossorigin=""/>
<script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js" integrity="sha512-XQoYMqMTK8LvdxXYG3nZ448hOEQiglfqkJs1NOQV44cWnUrBc8PkAOcXy20w0vlaXaVUearIOBhiXZ5V3ynxwA==" crossorigin=""></script>
<!-- fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Prosto+One&display=swap" rel="stylesheet">
<link href="../newsincerity.css" rel="stylesheet">
<style>
.bgimg-1 {bgimg} 

</style>
</head>
<body>

<div class="bgimg-1">
<div id="backwardlink"><a href="{url_left}" rel="{rel_left}" ><img src="../transparent.gif"></a></div>
<div id="forwardlink"><a href="{url_right}" rel="{rel_right}" ><img src="../transparent.gif">{right_frist_image}</a></div>
  <div class="caption">
    <span class="border">
	{caption}
	</span><br>
  </div>
</div>

<footer>
<div id="map" style="width: 100%; height: 400px;"></div>
<div id="copyright">
       <a rel="cc:attributionURL" property="dc:title">Photo</a> by
       <a rel="dc:creator" href=""
       property="cc:attributionName">Artem Svetlov</a> is licensed to the public under 
       the <a rel="license"
       href="https://creativecommons.org/licenses/by/4.0/">Creative
       Commons Attribution 4.0 License</a>.
</div>
<script>
{map_js}
</script>
{google_counter}
{yandex_counter}
</footer>
</body>
</html>

    
    '''
    return txt
    
    
json_dir = 'content'
output_directory = os.path.join(os.getcwd(), ".."+os.sep,'texts','t')
assert os.path.isdir(json_dir),'must exists directory "'+json_dir+'"'

json_files = [f for f in os.listdir(json_dir) if os.path.isfile(os.path.join(json_dir, f)) and f.lower().endswith('.json')]
assert len(json_files)>0,'must be find some .json files in '+json_dir

for json_filename in json_files:
    with open(os.path.join(json_dir,json_filename), encoding='utf-8') as json_file:
        data = json.load(json_file)
    assert data is not None
    
    # target directory
    output_directory_name = os.path.splitext(json_filename)[0]
    output_directory_path = os.path.join(output_directory,output_directory_name)

    
    assert os.path.isdir(output_directory_path), 'must exist directory '+output_directory_path
    
    template_filepath = 'gallery.template.htm'
    with open(template_filepath, encoding='utf-8') as template_file:
        template = template_file.read()
    assert '{image_url}' in template
    
    count_images = len(data['images'])
    current_image = 0
    
    for image in data['images']:
        current_image += 1
        
        if current_image < count_images:
            url_right = numfill(current_image+1)+'.htm'
            rel_right = 'next'
        else:
            url_right = 'index.htm'
            rel_right = 'up'
        if current_image > 1:
            url_left = numfill(current_image-1)+'.htm'
            rel_left = 'prev'
        else:
            url_left = 'index.htm'
            rel_left = 'up'
        
        if current_image == 1:
            right_frist_image = '''<img class="right_arrow" src="../click here to go next.svg">'''
        else:
            right_frist_image = ''
        
        map_js = '''
    var photo_coord = [55.666,37.666]
	var map = L.map('map').setView(['''+data['map_center']+'''], '''+data['map_zoom']+''');
	var OpenStreetMap_DE = L.tileLayer('https://{s}.tile.openstreetmap.de/tiles/osmde/{z}/{x}/{y}.png', {
		maxZoom: 18,
		attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
	});
	var tiles = OpenStreetMap_DE.addTo(map);
	var circle = L.circle(photo_coord, {
		color: 'red',
		fillColor: '#f03',
		fillOpacity: 0.5,
		radius: 200
	}).addTo(map).bindPopup('Гиперссылка на картографический сервис');
        '''
        
        html = str()
        
        template = template_remove_map(template)
        
        
        html = template.format(
        bgimg = '{  background-image: url("'+image['url']+'");  height: 100%;} ',
        caption = image['text'],
        url_left = url_left,
        url_right = url_right,
        rel_left = rel_left,
        rel_right = rel_right,
        map_js = map_js,
        right_frist_image = right_frist_image,
        google_counter = '''<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-119801939-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-119801939-1');
</script>''',
        yandex_counter = '''<!-- Yandex.Metrika counter -->
<script type="text/javascript" >
   (function(m,e,t,r,i,k,a){m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};
   m[i].l=1*new Date();k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)})
   (window, document, "script", "https://mc.yandex.ru/metrika/tag.js", "ym");

   ym(87742115, "init", {
        clickmap:true,
        trackLinks:true,
        accurateTrackBounce:true
   });
</script>
<noscript><div><img src="https://mc.yandex.ru/watch/87742115" style="position:absolute; left:-9999px;" alt="" /></div></noscript>
<!-- /Yandex.Metrika counter -->''',
        )
        
        filename = os.path.join(output_directory_path,numfill(current_image))+'.htm'
        with open(filename, "w", encoding='utf-8') as text_file:
            text_file.write(html)
