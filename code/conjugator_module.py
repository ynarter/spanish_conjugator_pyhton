# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 22:28:55 2021

@author: yigit
"""

def presente(verb1):
    l= len(verb1)
    end= verb1[l-2:l]
    verb= verb1[:l-2]
    if end== 'ar':
        s1= verb + 'o'
        s2= verb + 'as'
        s3= verb + 'a'
        p1= verb + 'amos'
        p2= verb + 'áis'
        p3= verb + 'an'
        print('yo',s1)
        print('tú',s2)
        print('él/ella/Vd.',s3)
        print('nosotros',p1)
        print('vosotros',p2)
        print('ellos/ellas/Vds.',p3)
    elif end== 'er':
        s1= verb + 'o'
        s2= verb + 'es'
        s3= verb + 'e'
        p1= verb + 'emos'
        p2= verb + 'éis'
        p3= verb + 'en'
        print('yo',s1)
        print('tú',s2)
        print('él/ella/Vd.',s3)
        print('nosotros',p1)
        print('vosotros',p2)
        print('ellos/ellas/Vds.',p3)
    elif end== 'ir':
        s1= verb + 'o'
        s2= verb + 'es'
        s3= verb + 'e'
        p1= verb + 'imos'
        p2= verb + 'ís'
        p3= verb + 'en'
        print('yo',s1)
        print('tú',s2)
        print('él/ella/Vd.',s3)
        print('nosotros',p1)
        print('vosotros',p2)
        print('ellos/ellas/Vds.',p3)



def indef(verb1):
    l= len(verb1)
    end= verb1[l-2:l]
    verb= verb1[:l-2]
    if end== 'ar':
        s1= verb + 'é'
        s2= verb + 'aste'
        s3= verb + 'ó'
        p1= verb + 'amos'
        p2= verb + 'asteis'
        p3= verb + 'aron'
        print('yo',s1)
        print('tú',s2)
        print('él/ella/Vd.',s3)
        print('nosotros',p1)
        print('vosotros',p2)
        print('ellos/ellas/Vds.',p3)
    elif end== 'er' or end== 'ir':
        s1= verb + 'í'
        s2= verb + 'iste'
        s3= verb + 'ió'
        p1= verb + 'imos'
        p2= verb + 'isteis'
        p3= verb + 'ieron'
        print('yo',s1)
        print('tú',s2)
        print('él/ella/Vd.',s3)
        print('nosotros',p1)
        print('vosotros',p2)
        print('ellos/ellas/Vds.',p3)
    
    
def imperf(verb1):
    l= len(verb1)
    end= verb1[l-2:l]
    verb= verb1[:l-2]
    if end== 'ar':
        s1= verb + 'aba'
        s2= verb + 'abas'
        s3= verb + 'aba'
        p1= verb + 'ábamos'
        p2= verb + 'abais'
        p3= verb + 'aban'
        print('yo',s1)
        print('tú',s2)
        print('él/ella/Vd.',s3)
        print('nosotros',p1)
        print('vosotros',p2)
        print('ellos/ellas/Vds.',p3)
    elif end== 'er' or end== 'ir':
        s1= verb + 'ía'
        s2= verb + 'ías'
        s3= verb + 'ía'
        p1= verb + 'íamos'
        p2= verb + 'íais'
        p3= verb + 'ían'
        print('yo',s1)
        print('tú',s2)
        print('él/ella/Vd.',s3)
        print('nosotros',p1)
        print('vosotros',p2)
        print('ellos/ellas/Vds.',p3)
    
def futuro(verb1):
        s1= verb1 + 'é'
        s2= verb1 + 'ás'
        s3= verb1 + 'á'
        p1= verb1 + 'emos'
        p2= verb1 + 'éis'
        p3= verb1 + 'án'
        print('yo',s1)
        print('tú',s2)
        print('él/ella/Vd.',s3)
        print('nosotros',p1)
        print('vosotros',p2)
        print('ellos/ellas/Vds.',p3)  
        
def condicional(verb):
        s1= verb + 'ía'
        s2= verb + 'ías'
        s3= verb + 'ía'
        p1= verb + 'íamos'
        p2= verb + 'íais'
        p3= verb + 'ían'
        print('yo',s1)
        print('tú',s2)
        print('él/ella/Vd.',s3)
        print('nosotros',p1)
        print('vosotros',p2)
        print('ellos/ellas/Vds.',p3)
        
        
def presente_subj(verb1):
    l= len(verb1)
    end= verb1[l-2:l]
    verb= verb1[:l-2]
    if end== 'ar':
        s1= verb + 'e'
        s2= verb + 'es'
        s3= verb + 'e'
        p1= verb + 'emos'
        p2= verb + 'éis'
        p3= verb + 'en'
        print('yo',s1)
        print('tú',s2)
        print('él/ella/Vd.',s3)
        print('nosotros',p1)
        print('vosotros',p2)
        print('ellos/ellas/Vds.',p3)

    elif end== 'er' or end== 'ir' :
        s1= verb + 'a'
        s2= verb + 'as'
        s3= verb + 'a'
        p1= verb + 'amos'
        p2= verb + 'áis'
        p3= verb + 'an'
        print('yo',s1)
        print('tú',s2)
        print('él/ella/Vd.',s3)
        print('nosotros',p1)
        print('vosotros',p2)
        print('ellos/ellas/Vds.',p3)
        
def imperf_subj(verb1):
    l= len(verb1)
    end= verb1[l-2:l]
    verb= verb1[:l-2]
    if end== 'ar':
        s1= verb + 'ara'
        s2= verb + 'aras'
        s3= verb + 'ara'
        p1= verb + 'áramos'
        p2= verb + 'arais'
        p3= verb + 'aran'
        print('yo',s1)
        print('tú',s2)
        print('él/ella/Vd.',s3)
        print('nosotros',p1)
        print('vosotros',p2)
        print('ellos/ellas/Vds.',p3)

    elif end== 'er' or end== 'ir' :
        s1= verb + 'iera'
        s2= verb + 'ieras'
        s3= verb + 'iera'
        p1= verb + 'iéramos'
        p2= verb + 'ierais'
        p3= verb + 'ieran'
        print('yo',s1)
        print('tú',s2)
        print('él/ella/Vd.',s3)
        print('nosotros',p1)
        print('vosotros',p2)
        print('ellos/ellas/Vds.',p3)
        
def imperf_subj_2(verb1):  
    l= len(verb1)
    end= verb1[l-2:l]
    verb= verb1[:l-2]
    if end== 'ar':
        s1= verb + 'ase'
        s2= verb + 'ases'
        s3= verb + 'ase'
        p1= verb + 'ásemos'
        p2= verb + 'aseis'
        p3= verb + 'asen'
        print('yo',s1)
        print('tú',s2)
        print('él/ella/Vd.',s3)
        print('nosotros',p1)
        print('vosotros',p2)
        print('ellos/ellas/Vds.',p3)

    elif end== 'er' or end== 'ir' :
        s1= verb + 'iese'
        s2= verb + 'ieses'
        s3= verb + 'iese'
        p1= verb + 'iésemos'
        p2= verb + 'ieseis'
        p3= verb + 'iesen'
        print('yo',s1)
        print('tú',s2)
        print('él/ella/Vd.',s3)
        print('nosotros',p1)
        print('vosotros',p2)
        print('ellos/ellas/Vds.',p3)
        

def perfecto_presente(verb1):
    l= len(verb1)
    end= verb1[l-2:l]
    verb= verb1[:l-2]
    if end== 'ar':
        verb= verb+'ado'
        s1= 'he '+verb
        s2= 'has '+verb
        s3= 'ha '+verb
        p1= 'hemos '+verb
        p2= 'habéis '+verb
        p3= 'han '+verb
        print('yo',s1)
        print('tú',s2)
        print('él/ella/Vd.',s3)
        print('nosotros',p1)
        print('vosotros',p2)
        print('ellos/ellas/Vds.',p3)

    elif end== 'er' or end== 'ir' :
        verb=verb+'ido'
        s1= 'he '+verb
        s2= 'has '+verb
        s3= 'ha '+verb
        p1= 'hemos '+verb
        p2= 'habéis '+verb
        p3= 'han '+verb
        print('yo',s1)
        print('tú',s2)
        print('él/ella/Vd.',s3)
        print('nosotros',p1)
        print('vosotros',p2)
        print('ellos/ellas/Vds.',p3)
        
def perfecto_pasado(verb1):
    l= len(verb1)
    end= verb1[l-2:l]
    verb= verb1[:l-2]
    if end== 'ar':
        verb= verb+'ado'
        s1= 'había '+verb
        s2= 'habías '+verb
        s3= 'había '+verb
        p1= 'habíamos '+verb
        p2= 'habíais '+verb
        p3='habían '+verb
        print('yo',s1)
        print('tú',s2)
        print('él/ella/Vd.',s3)
        print('nosotros',p1)
        print('vosotros',p2)
        print('ellos/ellas/Vds.',p3)

    elif end== 'er' or end== 'ir' :
        verb=verb+'ido'
        s1= 'había '+verb
        s2= 'habías '+verb
        s3= 'había '+verb
        p1= 'habíamos '+verb
        p2= 'habíais '+verb
        p3='habían '+verb
        print('yo',s1)
        print('tú',s2)
        print('él/ella/Vd.',s3)
        print('nosotros',p1)
        print('vosotros',p2)
        print('ellos/ellas/Vds.',p3)
        

def continuous(verb1):
    l= len(verb1)
    end= verb1[l-2:l]
    verb= verb1[:l-2]
    if end== 'ar':
        verb= verb+'ando'
        s1= 'estoy '+verb
        s2= 'estás '+verb
        s3= 'está '+verb
        p1= 'estamos '+verb
        p2= 'estáis '+verb
        p3='están '+verb
        print('yo',s1)
        print('tú',s2)
        print('él/ella/Vd.',s3)
        print('nosotros',p1)
        print('vosotros',p2)
        print('ellos/ellas/Vds.',p3)

    elif end== 'er' or end== 'ir' :
        verb=verb+'iendo'
        s1= 'estoy '+verb
        s2= 'estás '+verb
        s3= 'está '+verb
        p1= 'estamos '+verb
        p2= 'estáis '+verb
        p3='están '+verb
        print('yo',s1)
        print('tú',s2)
        print('él/ella/Vd.',s3)
        print('nosotros',p1)
        print('vosotros',p2)
        print('ellos/ellas/Vds.',p3)
        
        
def continuous_past(verb1):
    l= len(verb1)
    end= verb1[l-2:l]
    verb= verb1[:l-2]
    if end== 'ar':
        verb= verb+'ando'
        s1= 'estaba '+verb
        s2= 'estabas '+verb
        s3= 'estaba '+verb
        p1= 'estábamos '+verb
        p2= 'estabais '+verb
        p3='estaban '+verb
        print('yo',s1)
        print('tú',s2)
        print('él/ella/Vd.',s3)
        print('nosotros',p1)
        print('vosotros',p2)
        print('ellos/ellas/Vds.',p3)

    elif end== 'er' or end== 'ir' :
        verb=verb+'iendo'
        s1= 'estaba '+verb
        s2= 'estabas '+verb
        s3= 'estaba '+verb
        p1= 'estábamos '+verb
        p2= 'estabais '+verb
        p3='estaban '+verb
        print('yo',s1)
        print('tú',s2)
        print('él/ella/Vd.',s3)
        print('nosotros',p1)
        print('vosotros',p2)
        print('ellos/ellas/Vds.',p3)
        
        

    
        
        

   
