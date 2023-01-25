# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 22:10:55 2021

@author: yigit
"""
import conjugator_module





verb_s= input('Enter Spanish verb(regular): ')
while verb_s != '':
    k= len(verb_s)
    ending= verb_s[k-2:k]
    if ending != 'ar':
        if ending != 'er':
            if ending != 'ir':
                print('No es un verbo - Enter valid regular verb in Spanish!!')
        
            else:
                print('Presente de Indicativo del verbo',verb_s+':')
                spanish_conjugator.presente(verb_s)
                print('\nPretérito Indefinido del verbo',verb_s+':')
                spanish_conjugator.indef(verb_s)
                print('\nPretérito Imperfecto del verbo',verb_s+':')
                spanish_conjugator.imperf(verb_s)
                print('\nFuturo del verbo',verb_s+':')
                spanish_conjugator.futuro(verb_s)
                print('\nCondicional del verbo',verb_s+':')
                spanish_conjugator.condicional(verb_s)
                print('\nPresente de Subjuntivo del verbo',verb_s+':')
                spanish_conjugator.presente_subj(verb_s)
                print('\nPretérito Imperfecto de Subjuntivo del verbo',verb_s+':')
                spanish_conjugator.imperf_subj(verb_s)
                print('\nPretérito Imperfecto de Subjuntivo (2) del verbo',verb_s+':')
                spanish_conjugator.imperf_subj_2(verb_s)
                print('\nPretérito Perfecto del verbo',verb_s+':')
                spanish_conjugator.perfecto_presente(verb_s)
                print('\nPretérito Pluscuamperfecto del verbo',verb_s+':')
                spanish_conjugator.perfecto_pasado(verb_s)
                print('\nPresente Continúo del verbo',verb_s+':')
                spanish_conjugator.continuous(verb_s)
                print('\nPasado Continúo del verbo',verb_s+':')
                spanish_conjugator.continuous_past(verb_s)
    
        else:
            print('Presente de Indicativo del verbo',verb_s+':')
            spanish_conjugator.presente(verb_s)
            print('\nPretérito Indefinido del verbo',verb_s+':')
            spanish_conjugator.indef(verb_s)
            print('\nPretérito Imperfecto del verbo',verb_s+':')
            spanish_conjugator.imperf(verb_s)
            print('\nFuturo del verbo',verb_s+':')
            spanish_conjugator.futuro(verb_s)
            print('\nCondicional del verbo',verb_s+':')
            spanish_conjugator.condicional(verb_s)
            print('\nPresente de Subjuntivo del verbo',verb_s+':')
            spanish_conjugator.presente_subj(verb_s)
            print('\nPretérito Imperfecto de Subjuntivo del verbo',verb_s+':')
            spanish_conjugator.imperf_subj(verb_s)
            print('\nPretérito Imperfecto de Subjuntivo (2) del verbo',verb_s+':')
            spanish_conjugator.imperf_subj_2(verb_s)
            print('\nPretérito Perfecto del verbo',verb_s+':')
            spanish_conjugator.perfecto_presente(verb_s)
            print('\nPretérito Pluscuamperfecto del verbo',verb_s+':')
            spanish_conjugator.perfecto_pasado(verb_s)
            print('\nPresente Continúo del verbo',verb_s+':')
            spanish_conjugator.continuous(verb_s)
            print('\nPasado Continúo del verbo',verb_s+':')
            spanish_conjugator.continuous_past(verb_s)
    else:
        print('Presente de Indicativo del verbo',verb_s+':')
        spanish_conjugator.presente(verb_s)
        print('\nPretérito Indefinido del verbo',verb_s+':')
        spanish_conjugator.indef(verb_s)
        print('\nPretérito Imperfecto del verbo',verb_s+':')
        spanish_conjugator.imperf(verb_s)
        print('\nFuturo del verbo',verb_s+':')
        spanish_conjugator.futuro(verb_s)
        print('\nCondicional del verbo',verb_s+':')
        spanish_conjugator.condicional(verb_s)
        print('\nPresente de Subjuntivo del verbo',verb_s+':')
        spanish_conjugator.presente_subj(verb_s)
        print('\nPretérito Imperfecto de Subjuntivo del verbo',verb_s+':')
        spanish_conjugator.imperf_subj(verb_s)
        print('\nPretérito Imperfecto de Subjuntivo (2) del verbo',verb_s+':')
        spanish_conjugator.imperf_subj_2(verb_s)
        print('\nPretérito Perfecto del verbo',verb_s+':')
        spanish_conjugator.perfecto_presente(verb_s)
        print('\nPretérito Pluscuamperfecto del verbo',verb_s+':')
        spanish_conjugator.perfecto_pasado(verb_s)
        print('\nPresente Continúo del verbo',verb_s+':')
        spanish_conjugator.continuous(verb_s)
        print('\nPasado Continúo del verbo',verb_s+':')
        spanish_conjugator.continuous_past(verb_s)
    verb_s= input('Enter Spanish verb(regular): ')        
print('Gracias por usar')