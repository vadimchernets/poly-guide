#!/usr/bin/env python3
"""Poly A2: check one explicitly chosen UTF-8 CSV copy. No network or changes to input."""
import argparse
import csv
from decimal import Decimal, InvalidOperation
import json
from html import escape
import os
from pathlib import Path

# The report stays local, contains no scripts and preserves original column names.
REPORT_WORDS={
 'en':['Table check','File','Rows','Complete sum','Incomplete sum','No sum requested','Source line','Column','Issue','No structural issues found.','Compare the contents with the originals; this check does not prove the data is correct.','Missing value','Duplicate value','Invalid number','Wrong number of columns'],
 'ru':['Проверка таблицы','Файл','Строки','Полная сумма','Неполная сумма','Сумма не запрошена','Строка исходника','Столбец','Проблема','Ошибок структуры не найдено.','Сверьте содержание с оригиналами: эта проверка не доказывает достоверность данных.','Пропущенное значение','Повтор значения','Неверное число','Неверное число столбцов'],
 'zh':['表格检查','文件','行数','完整合计','不完整合计','未要求求和','源文件行号','列','问题','未发现结构问题。','请对照原始资料核实内容；此检查不能证明数据正确。','缺失值','重复值','无效数字','列数不正确'],
 'hi':['तालिका की जाँच','फ़ाइल','पंक्तियाँ','पूरा योग','अधूरा योग','योग निकालने का अनुरोध नहीं किया गया','स्रोत की पंक्ति','कॉलम','समस्या','ढाँचे में कोई समस्या नहीं मिली।','सामग्री का मूल स्रोतों से मिलान करें; यह जाँच डेटा के सही होने का प्रमाण नहीं है।','मान गायब है','दोहराया गया मान','अमान्य संख्या','कॉलम की संख्या गलत है'],
 'es':['Comprobación de tabla','Archivo','Filas','Suma completa','Suma incompleta','No se solicitó suma','Línea de origen','Columna','Problema','No se encontraron problemas de estructura.','Compara el contenido con los originales; esta comprobación no demuestra que los datos sean correctos.','Valor ausente','Valor duplicado','Número no válido','Número incorrecto de columnas'],
 'fr':['Vérification du tableau','Fichier','Lignes','Somme complète','Somme incomplète','Somme non demandée','Ligne source','Colonne','Problème','Aucun problème de structure détecté.','Comparez le contenu aux originaux ; cette vérification ne prouve pas que les données sont exactes.','Valeur manquante','Valeur en double','Nombre non valide','Nombre de colonnes incorrect'],
 'pt':['Verificação da tabela','Arquivo','Linhas','Soma completa','Soma incompleta','Soma não solicitada','Linha de origem','Coluna','Problema','Nenhum problema de estrutura encontrado.','Compare o conteúdo com os originais; esta verificação não comprova que os dados estão corretos.','Valor ausente','Valor duplicado','Número inválido','Quantidade incorreta de colunas'],
 'de':['Tabellenprüfung','Datei','Zeilen','Vollständige Summe','Unvollständige Summe','Keine Summe angefordert','Quellzeile','Spalte','Problem','Keine Strukturfehler gefunden.','Vergleichen Sie den Inhalt mit den Originalen; diese Prüfung beweist nicht die Richtigkeit der Daten.','Fehlender Wert','Doppelter Wert','Ungültige Zahl','Falsche Spaltenanzahl'],
 'ja':['表の確認','ファイル','行数','完全な合計','不完全な合計','合計は未指定','元ファイルの行','列','問題','構造上の問題は見つかりませんでした。','内容を原本と照合してください。この確認だけではデータの正しさは証明できません。','値が未入力','値が重複','無効な数値','列数が不正'],
 'ko':['표 확인','파일','행 수','전체 합계','불완전한 합계','합계 요청 없음','원본 행','열','문제','구조상의 문제가 발견되지 않았습니다.','내용을 원본과 대조하세요. 이 확인만으로 데이터가 정확하다고 증명되지는 않습니다.','누락된 값','중복된 값','잘못된 숫자','잘못된 열 수'],
 'uk':['Перевірка таблиці','Файл','Рядки','Повна сума','Неповна сума','Суму не запитано','Рядок джерела','Стовпець','Проблема','Структурних помилок не знайдено.','Звірте зміст з оригіналами: ця перевірка не доводить достовірність даних.','Пропущене значення','Повтор значення','Некоректне число','Неправильна кількість стовпців'],
}

def write_report(result, output, locale='en'):
    if locale not in REPORT_WORDS:raise ValueError('Unsupported report language')
    w=REPORT_WORDS[locale];e=lambda value:escape(str(value),quote=True)
    issue_names=dict(zip(['missing','duplicate','invalid-number','column-count'],w[11:]))
    rows=''.join('<tr><td>'+e(i['line'])+'</td><td>'+e(i.get('column','—'))+'</td><td>'+e(issue_names[i['issue']])+'</td></tr>' for i in result['issues'])
    summary=w[5] if result['sum'] is None else (w[3] if result['sumComplete'] else w[4])+': '+result['sum']+' ('+result['sumColumn']+')'
    html='<!doctype html><html lang="'+locale+'"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Poly A2 — '+e(w[0])+'</title><style>body{font:18px system-ui,sans-serif;max-width:850px;margin:32px auto;padding:0 20px;color:#172d25}h1{color:#146c43}table{border-collapse:collapse;width:100%}th,td{border:1px solid #aaa;padding:10px;text-align:left;overflow-wrap:anywhere}p{line-height:1.5}</style><h1>Poly A2 — '+e(w[0])+'</h1><p>'+e(w[1])+': '+e(result['file'])+'<br>'+e(w[2])+': '+e(result['rows'])+'</p><h2>'+e(summary)+'</h2>'
    html+=('<table><thead><tr>'+''.join('<th>'+e(label)+'</th>' for label in w[6:9])+'</tr></thead><tbody>'+rows+'</tbody></table>' if rows else '<p>'+e(w[9])+'</p>')+'<p>'+e(w[10])+'</p></html>'
    # Exclusive creation protects an existing result, including a symbolic link.
    fd=os.open(output,os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o600)
    with os.fdopen(fd,'w',encoding='utf-8') as target:target.write(html)
    return {'report':str(output),'locale':locale,'networkUsed':False,'inputChanged':False}


def check(filename, amount=None, identity=None, required=()):
    path=Path(filename)
    if path.is_symlink() or not path.is_file() or path.stat().st_size>2_000_000:
        raise ValueError('Choose a CSV copy up to 2 MB, not a link.')
    issues=[];values=[];seen={};total=Decimal(0)
    with path.open(encoding='utf-8-sig',newline='') as source:
        reader=csv.DictReader(source,strict=True)
        fields=reader.fieldnames
        if not fields or len(set(fields))!=len(fields):raise ValueError('The first row must have unique column names.')
        for column in [amount,identity,*required]:
            if column is not None and column not in fields:raise ValueError('Column not found: '+column)
        count=0
        for row in reader:
            count+=1
            if count>10000:raise ValueError('Choose a smaller table (up to 10000 rows).')
            line=reader.line_num
            if None in row or any(value is None for value in row.values()):issues.append({'line':line,'issue':'column-count'})
            for column in required:
                if not (row.get(column) or '').strip():issues.append({'line':line,'column':column,'issue':'missing'})
            if identity:
                key=(row.get(identity) or '').strip()
                if key and key in seen:issues.append({'line':line,'column':identity,'issue':'duplicate','firstLine':seen[key]})
                elif key:seen[key]=line
            if amount:
                raw=(row.get(amount) or '').strip()
                try:
                    if len(raw)>50:raise InvalidOperation
                    value=Decimal(raw)
                    if not value.is_finite() or abs(value)>Decimal('1e15') or value.as_tuple().exponent < -8:raise InvalidOperation
                    total+=value;values.append({'line':line,'value':str(value)})
                except InvalidOperation:issues.append({'line':line,'column':amount,'issue':'invalid-number'})
    return {'product':'Poly A2','file':path.name,'rows':count,'issues':issues,'sum':str(total) if amount else None,'sumColumn':amount,'includedValues':values,'sumComplete':not any(i['issue'] in ('invalid-number','column-count') for i in issues),'sourceCheckRequired':True,'networkUsed':False,'inputChanged':False}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--file',required=True);parser.add_argument('--amount-column');parser.add_argument('--id-column');parser.add_argument('--required',action='append',default=[])
    parser.add_argument('--html',help='Create a new local readable report; never replace an existing file')
    parser.add_argument('--locale',choices=REPORT_WORDS,default='en')
    args=parser.parse_args()
    try:
        result=check(args.file,args.amount_column,args.id_column,args.required)
        if args.html:result['readableReport']=write_report(result,args.html,args.locale)
    except (ValueError,OSError,UnicodeError,csv.Error) as error:parser.exit(1,str(error)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
