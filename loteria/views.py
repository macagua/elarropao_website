# -*- coding: utf-8 -*-

from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from elarropao.loteria.models import Publicidad, Loteria, Sorteo, Resultado_Triple, Resultado_Kino, Resultado_Triple_Gordo, Resultado_Papaya, Noticia
from datetime import datetime
import time
from django.conf import settings
from django.db.models import Q
from elarropao.loteria.forms import ContactoForm
from django.core.mail import send_mail
from django.conf import settings
from django.utils.text import *
from django.contrib.sites.models import Site

def index(request):
    return render_to_response('loteria/index.html', {})

def sorteo(request, id):
    resultados = Resultado_Triple.objects.filter(sorteo=id).order_by('-fecha')[:10]
    
    if resultados:
        sorteo = Sorteo.objects.get(id=id)
        return render_to_response('loteria/sorteo.html', {'loteria': sorteo.loteria.nombre, 'sorteo': sorteo.nombre, 'resultados': resultados})
    else:
        return render_to_response('loteria/sorteo.html', {'noresultado': True})
    
    
def triples(request):
    publicidad_derecha = Publicidad.objects.filter(contenedor=1).order_by('orden')
    publicidad_izquierda = Publicidad.objects.filter(contenedor=2).order_by('orden')
    fecha = datetime.now()
    noticia = Noticia.objects.filter(publicar=True)
    #fecha_ayer = datetime.fromtimestamp(time.time()-86400)
    loteria = Loteria.objects.all().order_by('nombre')
    visitas_site = Site.objects.get(id=1)
    
    html_resultado = ''
    html_noticia = ''
    enlace = '<a href="/loteria/otros/"><strong>Resultados Kino, Triple Gordo</strong></a>'
    
    if noticia:
        for i in noticia:

            html_noticia += '''
        <table id="" class="table">
        '''

            html_noticia += '''
            <tr>
                <td class="td_255"><img src="%simg/Cobijazos.gif" /></td>
                <td class="titulo_sorteo center_text td_255"><pre>%s</pre></td>
            </tr>
            <tr>
                <td colspan="2">
                    <pre>%s</pre>
                </td>
            </tr>
            ''' % (settings.MEDIA_URL, wrap(i.titulo, 15), wrap(i.nota, 70))
            html_noticia += '''
        </table>
        <br />
        '''
        
    for i in loteria:
        
        if i.sorteo_set.filter(tipo=1):
        
            html_resultado += '''
            <table id= "" class="table">'''
            html_resultado += '''
            <tr>
                <td class="td_255">
                    <img src="%s" />
                </td>
                <td class="titulo_sorteo td_255">
                    <h1>%s</h1>
                </td>
            </tr>
            ''' % (i.imagen.url, i.nombre)
            
            #Triples
            if i.sorteo_set.filter(tipo=1):
                html_resultado += '''
                    <tr>
                    <td colspan="2">
                    <table id="" class="table1">
                        <tr>
                            <td class="center_text td_166 titulo_resultado"><h2>Sorteo</h2></td>
                            <td class="center_text td_80 titulo_resultado"><h2>Fecha</h2></td>
                            <td class="center_text td_80 titulo_resultado"><h2>Hora</h2></td>
                            <td class="center_text td_80 titulo_resultado"><h2>N&#250;mero</h2></td>
                            <td class="center_text td_80 titulo_resultado"><h2>Resultados Anteriores</h2></td>
                        </tr>
                '''
                    
                for j in i.sorteo_set.filter(tipo=1):

#                    result = Resultado_Triple.objects.filter(sorteo=j).filter(Q(fecha=fecha)).order_by('-fecha')
                    result = Resultado_Triple.objects.filter(sorteo=j).filter(Q(fecha='2010-07-28')).order_by('-fecha')
#                    result = Resultado_Triple.objects.filter(sorteo=j).order_by(j.hora,j.nombre)
                    
                    html_resultado += '''
                    <tr>'''
                    
                    if result:
        
                        for k in result:
                            numero = k.numero
                            
                            if k.animalito.nombre <> "Ninguno":
                                numero += ' - %s' %  k.animalito.nombre
                            if k.signo.nombre <> "Ninguno":
                                numero += ' - %s' % k.signo.nombre
                            
                            consultar_anterior = '<img onclick="%s" src="%simg/previo.png" />' % ("javascript:window.open('/sorteo/%s','popup','toolbar=no,location=no,status=no,menubar=no,scrollbars=yes,resizable=no,width=400,height=300')" % j.id, settings.MEDIA_URL)
                            
                            html_resultado += '''
                                <tr>
                                    <td class="td_166">%s</td>
                                    <td class="center_text td_80">%s</td>
                                    <td class="center_text td_80">%s</td>
                                    <td class="center_text td_80">%s</td>
                                    <td class="center_text td_80">%s</td>
                                </tr>''' % (j.nombre,k.fecha.strftime('%d-%m-%Y'), j.hora.strftime('%I:%M %p'), numero, consultar_anterior)
                        
                    else:
                        html_resultado += '''
                        <tr>
                            <td class="td_166">%s</td>
                            
                            <td class="center_text" colspan="3">
                                No Existen Resultados
                            </td>
                            <td class="center_text">
                                <img onclick="%s" src="%simg/previo.png" />
                            </td>
                        </tr>
                        ''' % (j.nombre, "javascript:window.open('/sorteo/%s','popup','toolbar=no,location=no,status=no,menubar=no,scrollbars=yes,resizable=no,width=400,height=300')" % j.id, settings.MEDIA_URL)
        
        
                    html_resultado += '''
                    </tr>'''
        
                html_resultado += '''
                            </table>
                            </td>
                            </tr>'''
    
    
       
            html_resultado += '''
            </table>
            <br />
        '''

    return render_to_response('loteria/loteria.html', {'publicidad_derecha': publicidad_derecha,'publicidad_izquierda': publicidad_izquierda, 'fecha': fecha, 'resultados': html_resultado, 'noticias': html_noticia, 'visitas_site': visitas_site, 'enlace': enlace})



def otros(request):
    publicidad_derecha = Publicidad.objects.filter(contenedor=1).order_by('orden')
    publicidad_izquierda = Publicidad.objects.filter(contenedor=2).order_by('orden')
    fecha = datetime.now()
    noticia = Noticia.objects.filter(publicar=True)
    #fecha_ayer = datetime.fromtimestamp(time.time()-86400)
    loteria = Loteria.objects.all().order_by('nombre')
    visitas_site = Site.objects.get(id=1)
    
    html_resultado = ''
    html_noticia = ''
    enlace = '<a href="/loteria/triples/"><strong>Resultados Triples</strong></a>'
    
    #if noticia:
    #    for i in noticia:
    #
    #        html_noticia += '''
    #    <table id="" class="table">
    #    '''
    #
    #        html_noticia += '''
    #        <tr>
    #            <td class="td_255"><img src="%simg/Cobijazos.gif" /></td>
    #            <td class="titulo_sorteo center_text td_255"><pre>%s</pre></td>
    #        </tr>
    #        <tr>
    #            <td colspan="2">
    #                <pre>%s</pre>
    #            </td>
    #        </tr>
    #        ''' % (settings.MEDIA_URL, wrap(i.titulo, 15), wrap(i.nota, 70))
    #        html_noticia += '''
    #    </table>
    #    <br />
    #    '''
        
    for i in loteria:
        
        if i.sorteo_set.filter(tipo=4) or i.sorteo_set.filter(tipo=3) or i.sorteo_set.filter(tipo=2):
            
            html_resultado += '''
            <table id= "" class="table">'''
            html_resultado += '''
            <tr>
                <td class="td_255">
                    <img src="%s" />
                </td>
                <td class="titulo_sorteo td_255">
                    <h1><label>%s</label></h1>
                </td>
            </tr>
            ''' % (i.imagen.url, i.nombre)
            
            #Papaya
            if i.sorteo_set.filter(tipo=4):
                for j in i.sorteo_set.filter(tipo=4):
                    html_resultado += '''
                    <tr>
                    <td colspan="2" class="center_text">
                        <h1>%s</h1>
                    </td>
                    ''' % (j.nombre)
                    
                    html_resultado += '''
                    </tr>
                    <tr>
                    <td colspan="2" class="center_text">
                    '''
        
                    result_papaya = Resultado_Papaya.objects.filter(sorteo=j).order_by('-id')[:1]
                    if result_papaya:
                        result_papaya = result_papaya.get()
                        
                        html_resultado += '''
                    <table id="" class="table">
                        <tr>
                            <td colspan="3" class="center_text">
                                <img src="%s" />
                                <h2>Sorteo N. %s - Fecha: %s</h2>
                            </td>
                        </tr>
                        <tr>
                            <td colspan="3" class="center_text titulo_resultado">
                                <h1>TRIPLE TERMINAL</h1>
                            </td>
                        </tr>
                        <tr class="center_text">
                                <td>
                                    <h1>A: %s</h1>
                                </td>
                                <td>
                                    <h1>B: %s</h1>
                                </td>
                                <td>
                                    <h1>C: %s</h1>
                                </td>
                        </tr>
                        <tr>
                            <td colspan="3" class="center_text titulo_resultado">
                                <h1>DOBLETE</h1>
                            </td>
                        </tr>
                        <tr class="center_text">
                            <td>
                                <h1>A: %s-%s</h1>
                            </td>
                            <td>
                                <h1>B: %s-%s</h1>
                            </td>
                            <td>
                                <h1>C: %s-%s</h1>
                            </td>
                        </tr>
                        <tr>
                            <td colspan="3" class="center_text titulo_resultado">
                                <h1>SENCILLO</h1>
                            </td>
                        </tr>
                        <tr>
                            <td colspan="3" class="center_text">
                                <h1>%s</h1>
                            </td>
                        </tr>
                    </table>
                        ''' % ("/site_media/img/papaya.jpg", 
                               result_papaya.numero_sorteo, 
                               result_papaya.fecha.strftime('%d-%m-%Y'), 
                               result_papaya.triple_terminal_a, 
                               result_papaya.triple_terminal_b, 
                               result_papaya.triple_terminal_c, 
                               result_papaya.doblete_a_a, 
                               result_papaya.doblete_a_b, 
                               result_papaya.doblete_b_a, 
                               result_papaya.doblete_b_b, 
                               result_papaya.doblete_c_a, 
                               result_papaya.doblete_c_b, 
                               result_papaya.sencillo )
                    else:
                        html_resultado += '''
                        No Existen Resultados
                        '''
                    
                    html_resultado += '''
                    </td>
                    </tr>
                    '''
    
            #Triple Gordo
            if i.sorteo_set.filter(tipo=3):
                for j in i.sorteo_set.filter(tipo=3):
                    html_resultado += '''
                    <tr>
                    <td colspan="2" class="center_text">
                        <h1>%s</h1>
                    </td>
                    ''' % (j.nombre)
                    
                    html_resultado += '''
                    </tr>
                    <tr>
                    <td colspan="2" class="center_text">
                    '''
        
                    result_triple_gordo = Resultado_Triple_Gordo.objects.filter(sorteo=j).order_by('-id')[:1]
                    
                    if result_triple_gordo:
                        result_triple_gordo = result_triple_gordo.get()
                        
                        html_resultado += '''
                        <table id="" class="table">
                            <tr>
                                <td colspan="3">
                                    <img src="%s" />
                                    <h2>Sorteo N. %s - Domingo, %s - Color %s</h2>
                                </td>
                            </tr>
                            <tr>
                                <td colspan="3" class="titulo_resultado center_text">
                                    <h1>SUPER DUPLETA</h1> 
                                </td>
                            </tr>
                            <tr class="titulo_resultado center_text">
                                <td>
                                    <h1>TRIPLE 1</h1>
                                </td>
                                <td>
                                    <h1>TRIPLE 2</h1>
                                </td>
                                <td>
                                    <h1>TRIPLE 3</h1>
                                </td>
                            </tr>
                            <tr class="center_text">
                                <td>
                                    <h1>%s</h1>
                                </td>
                                <td>
                                    <h1>%s</h1>
                                </td>
                                <td>
                                    <h1>%s</h1>
                                </td>
                            </tr>
                            <tr>
                                <td colspan="3" class="titulo_resultado center_text">
                                    <h1>ESPECIAL CANTADO</h1>
                                </td>
                            </tr>
                            <tr>
                                <td colspan="3" class="center_text">
                                    <h1>%s</h1>
                                </td>
                            </tr>
                            <tr>
                                <td colspan="3" class="titulo_resultado center_text">
                                    <h1>PAR MILLONARIO</h1>
                                </td>
                            </tr>
                            <tr>
                                <td colspan="3" class="center_text">
                                    <h1><font color="blue">A:</font> %s / <font color="red">B:</font> %s</h1>
                                </td>
                            </tr>
                        </table>
                        ''' % ("/site_media/img/triplegordo.gif",
                               result_triple_gordo.numero_sorteo, 
                               result_triple_gordo.fecha.strftime('%d / %m / %Y'), 
                               result_triple_gordo.color, 
                               result_triple_gordo.super_dupleta_1, 
                               result_triple_gordo.super_dupleta_2, 
                               result_triple_gordo.super_dupleta_3, 
                               result_triple_gordo.especial_cantado, 
                               result_triple_gordo.par_millonario_a, 
                               result_triple_gordo.par_millonario_b)
                    else:
                        html_resultado += '''
                        No Existen Resultados
                        '''
                    
                    
                    html_resultado += '''
                    </td>
                    </tr>
                    '''
           
            #Kino
            if i.sorteo_set.filter(tipo=2):
                for j in i.sorteo_set.filter(tipo=2):
                    html_resultado += '''
                    <tr>
                    <td colspan="2" class="center_text">
                        <h1>%s</h1>
                    </td>
                    ''' % (j.nombre)
                    
                    html_resultado += '''
                    </tr>
                    <tr>
                    <td colspan="2" class="center_text">
                    '''
        
                    result_kino = Resultado_Kino.objects.filter(sorteo=j).order_by('-id')[:1]
                    if result_kino:
                        result_kino = result_kino.get()
                        html_resultado += '''
                        <table id="" class="table1">
                            <tr>
                                <td colspan="3" class="center_text">
                                    <img src="%s" />
                                    <h2>Sorteo: %s - Domingo, %s</h2>
                                </td>
                            </tr>
                            <tr class="center_text">
                                <td><h1>%s</h1></td>
                                <td><h1>%s</h1></td>
                                <td><h1>%s</h1></td>
                            </tr>
                            <tr class="center_text">
                                <td><h1>%s</h1></td>
                                <td><h1>%s</h1></td>
                                <td><h1>%s</h1></td>
                            </tr>
                            <tr class="center_text">
                                <td><h1>%s</h1></td>
                                <td><h1>%s</h1></td>
                                <td><h1>%s</h1></td>
                            </tr>
                            <tr class="center_text">
                                <td><h1>%s</h1></td>
                                <td><h1>%s</h1></td>
                                <td><h1>%s</h1></td>
                            </tr>
                            <tr class="center_text">
                                <td><h1>%s</h1></td>
                                <td><h1>%s</h1></td>
                                <td><h1>%s</h1></td>
                            </tr>
                            
                        </table>
                        ''' % ("/site_media/img/kino.gif", 
                               result_kino.numero_sorteo, 
                               result_kino.fecha.strftime('%d-%m-%Y'), 
                               result_kino.numero1, 
                               result_kino.numero2, 
                               result_kino.numero3, 
                               result_kino.numero4, 
                               result_kino.numero5, 
                               result_kino.numero6, 
                               result_kino.numero7, 
                               result_kino.numero8, 
                               result_kino.numero9, 
                               result_kino.numero10, 
                               result_kino.numero11, 
                               result_kino.numero12, 
                               result_kino.numero13, 
                               result_kino.numero14, 
                               result_kino.numero15)
                    else:
                        html_resultado += '''
                        <h1>No Existen Resultados</h1>
                        '''
                    
                    
                    html_resultado += '''
                    </td>
                    </tr>
                    '''
                
    
       
            html_resultado += '''
            </table>
            <br />
        '''

    return render_to_response('loteria/loteria.html', {'publicidad_derecha': publicidad_derecha,'publicidad_izquierda': publicidad_izquierda, 'fecha': fecha, 'resultados': html_resultado, 'noticias': html_noticia, 'visitas_site': visitas_site, 'enlace': enlace})


def contacto(request):
    publicidad_derecha = Publicidad.objects.filter(contenedor=1).order_by('orden')
    publicidad_izquierda = Publicidad.objects.filter(contenedor=2).order_by('orden')
    fecha = datetime.now()

    if request.method == "POST":
        
        form = ContactoForm(request.POST)
        
        asunto = form['asunto'].data
        mensaje = form['mensaje'].data
        email = form['email'].data
        
        if form.is_valid():
            send_mail(asunto, mensaje, email, [settings.CONTACTO[0][1]])
            return render_to_response('mensajes.html', {'mensaje': 'Estamos procesando su mensaje, gracias...', 'publicidad_derecha': publicidad_derecha,'publicidad_izquierda': publicidad_izquierda})
        else:
            return render_to_response('contacto/contacto.html', {'form': form, 'publicidad_derecha': publicidad_derecha,'publicidad_izquierda': publicidad_izquierda})

    else:
        
        form = ContactoForm()
        return render_to_response('contacto/contacto.html', {'form': form, 'publicidad_derecha': publicidad_derecha,'publicidad_izquierda': publicidad_izquierda})
