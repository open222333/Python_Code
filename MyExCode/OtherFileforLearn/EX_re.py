import re

# 函數	說明
# compile(pattern)	以配對形式字串 pattern 當參數，回傳 re.compile() 物件。
# search(pattern, string, flags=0)	從 string 中找尋第一個配對形式字串 pattern ，找到回傳配對物件，沒有找到回傳 None 。
# match(pattern, string, flags=0)	判斷配對形式字串 pattern 是否與 string 的開頭相符，如果相符就回傳配對物件，不相符就回傳 None 。
# fullmatch(pattern, string, flags=0)	判斷 string 是否與配對形式字串 pattern 完全相符，如果完全相符就回傳配對物件，不完全相符就回傳 None 。
# split(pattern, string, maxsplit=0, flags=0)	將 string 以配對形式字串 pattern 拆解，結果回傳拆解後的串列。
# findall(pattern, string, flags=0)	從 string 中找到所有的 pattern ，結果回傳所有 pattern 的串列。
# finditer(pattern, string, flags=0)	從 string 中找到所有的 pattern ，結果回傳所有 pattern 的迭代器。
# sub(pattern, repl, string, count=0, flags=0)	依據 pattern 及 repl 對 string 進行處理，結果回傳處理過的新字串。
# subn(pattern, repl, string, count=0, flags=0)	依據 pattern 及 repl 對 string 進行處理，結果回傳處理過的序對。
# escape(pattern)	將 pattern 中的特殊字元加入反斜線，結果回傳新字串。
# purge()	清除正規運算式的內部緩存。

testdata = ['https://www.example.com/25213/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2%e0%b8%a5%e0%b9%88%e0%b8%ad%e0%b8%ab%e0%b8%b5%e0%b8%82%e0%b8%ad%e0%b8%87%e0%b8%aa%e0%b8%b2%e0%b8%a7%e0%b8%99/', 'https://www.example.com/25152/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2%e0%b8%84%e0%b8%99%e0%b8%ab%e0%b8%99%e0%b8%b8%e0%b9%88%e0%b8%a1%e0%b8%aa%e0%b8%b2%e0%b8%a7%e0%b9%84%e0%b8%9b/', 'https://www.example.com/25125/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2%e0%b8%88%e0%b8%b1%e0%b8%94%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%81%e0%b8%aa%e0%b8%b2%e0%b8%a7%e0%b8%a1%e0%b8%ab/', 'https://www.example.com/25103/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2%e0%b8%97%e0%b8%b2%e0%b8%87%e0%b8%9a%e0%b9%89%e0%b8%b2%e0%b8%99%e0%b8%88%e0%b8%b1%e0%b8%94%e0%b8%ab%e0%b8%99/', 'https://www.example.com/25088/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2%e0%b8%ab%e0%b8%b5%e0%b8%ad%e0%b8%a2%e0%b9%88%e0%b8%b2%e0%b8%87%e0%b8%9f%e0%b8%b4%e0%b8%95%e0%b9%80%e0%b8%a5/', 'https://www.example.com/24992/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2%e0%b9%80%e0%b8%a1%e0%b8%b2%e0%b9%81%e0%b8%a5%e0%b9%89%e0%b8%a7%e0%b9%80%e0%b8%87%e0%b8%b5%e0%b9%88%e0%b8%a2/', 'https://www.example.com/24986/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2%e0%b8%a2%e0%b8%b1%e0%b9%88%e0%b8%a7%e0%b9%81%e0%b8%9f%e0%b8%99%e0%b8%ab%e0%b8%99%e0%b8%b8%e0%b9%88%e0%b8%a1/', 'https://www.example.com/24984/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2%e0%b8%84%e0%b8%a5%e0%b8%b4%e0%b8%9b%e0%b9%80%e0%b8%a2%e0%b9%87%e0%b8%94%e0%b9%80%e0%b8%a1%e0%b8%b5%e0%b8%a2/', 'https://www.example.com/24978/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2%e0%b8%88%e0%b8%b1%e0%b8%94%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%81%e0%b8%81%e0%b8%b1%e0%b8%9a%e0%b9%81%e0%b8%9f/', 'https://www.example.com/24955/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2%e0%b9%80%e0%b8%94%e0%b9%87%e0%b8%81%e0%b8%ab%e0%b8%99%e0%b8%b8%e0%b9%88%e0%b8%a1%e0%b8%aa%e0%b8%b2%e0%b8%a7/', 'https://www.example.com/24902/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2%e0%b8%ad%e0%b8%a2%e0%b9%88%e0%b8%b2%e0%b8%87%e0%b8%a2%e0%b8%b1%e0%b9%88%e0%b8%a7%e0%b9%80%e0%b8%a5%e0%b8%a2/', 'https://www.example.com/24867/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2%e0%b8%aa%e0%b8%b2%e0%b8%a7%e0%b8%8a%e0%b8%b8%e0%b8%94%e0%b8%95%e0%b8%b2%e0%b8%82%e0%b9%88%e0%b8%b2%e0%b8%a2/', 'https://www.example.com/24855/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2%e0%b9%80%e0%b8%88%e0%b9%8a%e0%b8%a7%e0%b8%b4-%e0%b8%aa%e0%b8%b2%e0%b8%a7%e0%b9%83%e0%b8%ab%e0%b8%8d%e0%b9%88/', 'https://www.example.com/24842/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2%e0%b8%aa%e0%b8%b2%e0%b8%a7%e0%b9%80%e0%b8%aa%e0%b8%b7%e0%b9%89%e0%b8%ad%e0%b8%8a%e0%b8%a1%e0%b8%9e%e0%b8%b9/', 'https://www.example.com/24787/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2%e0%b8%99%e0%b9%89%e0%b8%ad%e0%b8%87%e0%b9%80%e0%b8%a1%e0%b8%b5%e0%b8%a2%e0%b9%80%e0%b8%94%e0%b9%87%e0%b8%94/', 'https://www.example.com/24775/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2%e0%b9%80%e0%b8%87%e0%b8%b5%e0%b9%88%e0%b8%a2%e0%b8%99%e0%b8%aa%e0%b8%b2%e0%b8%a7%e0%b8%97%e0%b8%b2%e0%b8%87/', 'https://www.example.com/24757/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2%e0%b8%aa%e0%b8%b2%e0%b8%a7%e0%b8%84%e0%b8%99%e0%b8%99%e0%b8%b5%e0%b9%89%e0%b8%8a%e0%b9%88%e0%b8%a7%e0%b8%a2/', 'https://www.example.com/24702/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2%e0%b8%99%e0%b8%b1%e0%b8%81%e0%b9%80%e0%b8%a3%e0%b8%b5%e0%b8%a2%e0%b8%99%e0%b8%ad%e0%b8%a2%e0%b8%b2%e0%b8%81/', 'https://www.example.com/24676/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2%e0%b9%80%e0%b8%a5%e0%b9%88%e0%b8%99%e0%b8%ab%e0%b8%b5%e0%b8%ad%e0%b8%a2%e0%b9%88%e0%b8%b2%e0%b8%87%e0%b9%80/', 'https://www.example.com/24670/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2%e0%b9%80%e0%b8%aa%e0%b8%b5%e0%b8%a2%e0%b8%a7%e0%b9%80%e0%b8%81%e0%b8%b4%e0%b8%99%e0%b8%9a%e0%b8%a3%e0%b8%a3/', 'https://www.example.com/24650/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2%e0%b8%81%e0%b8%a3%e0%b8%b0%e0%b9%81%e0%b8%97%e0%b8%81%e0%b8%ab%e0%b8%b5%e0%b8%ad%e0%b8%a2%e0%b9%88%e0%b8%b2/', 'https://www.example.com/24623/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2%e0%b8%aa%e0%b8%b2%e0%b8%a7%e0%b8%9c%e0%b8%a1%e0%b8%aa%e0%b8%b1%e0%b9%89%e0%b8%99%e0%b8%aa%e0%b8%b8%e0%b8%94/', 'https://www.example.com/24613/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2%e0%b8%aa%e0%b8%b2%e0%b8%a7%e0%b8%aa%e0%b8%a7%e0%b8%a2%e0%b8%a1%e0%b8%b2%e0%b9%82%e0%b8%8a%e0%b8%a7%e0%b9%8c/',
            'https://www.example.com/24609/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2%e0%b8%aa%e0%b8%b2%e0%b8%a7%e0%b8%99%e0%b9%89%e0%b8%ad%e0%b8%a2%e0%b8%82%e0%b9%89%e0%b8%b2%e0%b8%87%e0%b8%9a/', 'https://www.example.com/24578/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2%e0%b8%96%e0%b9%89%e0%b8%b2%e0%b8%88%e0%b8%b0%e0%b8%95%e0%b9%89%e0%b8%ad%e0%b8%87%e0%b8%81%e0%b8%b2%e0%b8%a3/', 'https://www.example.com/24469/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2%e0%b8%a2%e0%b8%b1%e0%b9%88%e0%b8%a7%e0%b8%88%e0%b8%a3%e0%b8%b4%e0%b8%87%e0%b9%86%e0%b9%80%e0%b8%a5%e0%b8%a2/', 'https://www.example.com/24459/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2%e0%b9%84%e0%b8%a1%e0%b9%88%e0%b8%a3%e0%b8%b9%e0%b9%89%e0%b9%80%e0%b8%82%e0%b8%b2%e0%b9%80%e0%b8%87%e0%b8%b5/', 'https://www.example.com/24447/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2%e0%b8%aa%e0%b8%b2%e0%b8%a7%e0%b9%83%e0%b8%ab%e0%b8%8d%e0%b9%88%e0%b9%80%e0%b8%98%e0%b8%ad%e0%b8%81%e0%b8%b3/', 'https://www.example.com/24505/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2%e0%b9%80%e0%b8%ad%e0%b8%b2%e0%b8%aa%e0%b8%b2%e0%b8%a7%e0%b9%83%e0%b8%99%e0%b8%a7%e0%b8%b1%e0%b8%99%e0%b8%84/', 'https://www.example.com/24501/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2%e0%b8%81%e0%b8%b0%e0%b8%ab%e0%b8%a3%e0%b8%b5%e0%b9%88%e0%b8%aa%e0%b8%b2%e0%b8%a7%e0%b9%80%e0%b8%a1%e0%b8%b7/', 'https://www.example.com/24497/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2%e0%b8%99%e0%b8%b1%e0%b8%81%e0%b8%a8%e0%b8%b6%e0%b8%81%e0%b8%a9%e0%b8%b2%e0%b8%aa%e0%b8%b2%e0%b8%a7%e0%b9%80/', 'https://www.example.com/24481/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2%e0%b9%82%e0%b8%8a%e0%b8%a7%e0%b9%8c%e0%b9%80%e0%b8%aa%e0%b8%b5%e0%b8%a2%e0%b8%a7-%e0%b8%95%e0%b8%b4%e0%b9%89/', 'https://www.example.com/24479/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2%e0%b8%9e%e0%b8%b2%e0%b8%aa%e0%b8%b2%e0%b8%a7%e0%b8%ab%e0%b8%b8%e0%b9%88%e0%b8%99%e0%b8%aa%e0%b8%a7%e0%b8%a2/', 'https://www.example.com/24375/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2-%e0%b8%a5%e0%b9%88%e0%b8%ad%e0%b8%ab%e0%b8%b5%e0%b8%82%e0%b8%ad%e0%b8%87%e0%b8%aa%e0%b8%b2%e0%b8%a7%e0%b9%83/', 'https://www.example.com/24305/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2-%e0%b9%82%e0%b8%94%e0%b8%99%e0%b8%84%e0%b8%a7%e0%b8%a2%e0%b9%83%e0%b8%ab%e0%b8%8d%e0%b9%88-%e0%b8%a1%e0%b8%b1/', 'https://www.example.com/24297/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2-%e0%b8%94%e0%b8%b4%e0%b8%a5%e0%b9%82%e0%b8%94%e0%b9%89%e0%b8%82%e0%b8%ad%e0%b8%87%e0%b9%80%e0%b8%98%e0%b8%ad/', 'https://www.example.com/24295/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2-%e0%b8%96%e0%b9%88%e0%b8%b2%e0%b8%a2%e0%b9%81%e0%b8%9a%e0%b8%9a%e0%b8%99%e0%b8%b9%e0%b9%89%e0%b8%94%e0%b8%aa/', 'https://www.example.com/24291/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2-%e0%b8%84%e0%b8%b7%e0%b8%99%e0%b8%a7%e0%b8%b1%e0%b8%99%e0%b9%80%e0%b8%82%e0%b9%89%e0%b8%b2%e0%b8%ab%e0%b8%ad/', 'https://www.example.com/24277/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2-%e0%b8%ab%e0%b8%99%e0%b9%89%e0%b8%b2%e0%b8%95%e0%b8%b2%e0%b8%ad%e0%b8%a2%e0%b9%88%e0%b8%b2%e0%b8%87%e0%b8%aa/', 'https://www.example.com/24271/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2%e0%b9%80%e0%b8%a2%e0%b9%87%e0%b8%94%e0%b8%ab%e0%b8%b5%e0%b8%81%e0%b8%b0%e0%b8%ab%e0%b8%a3%e0%b8%b5%e0%b9%88/', 'https://www.example.com/19940/xxx%e0%b9%80%e0%b8%94%e0%b9%87%e0%b8%81%e0%b8%aa%e0%b8%b2%e0%b8%a7%e0%b8%99%e0%b9%89%e0%b8%ad%e0%b8%a2%e0%b8%ad%e0%b8%a2%e0%b8%b2%e0%b8%81%e0%b8%88%e0%b8%b0%e0%b8%a5%e0%b8%ad%e0%b8%87%e0%b8%94/', 'https://www.example.com/24775/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2%e0%b9%80%e0%b8%87%e0%b8%b5%e0%b9%88%e0%b8%a2%e0%b8%99%e0%b8%aa%e0%b8%b2%e0%b8%a7%e0%b8%97%e0%b8%b2%e0%b8%87/', 'https://www.example.com/20670/%e0%b8%84%e0%b8%a5%e0%b8%b4%e0%b8%9b%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%80%e0%b8%94%e0%b9%87%e0%b8%81%e0%b8%aa%e0%b8%9a%e0%b8%b2%e0%b8%a2%e0%b9%83%e0%b8%88%e0%b9%80%e0%b8%a5%e0%b8%a2%e0%b8%97%e0%b8%b5/', 'https://www.example.com/24963/%e0%b8%84%e0%b8%a5%e0%b8%b4%e0%b8%9b%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2%e0%b8%84%e0%b8%a5%e0%b8%b4%e0%b8%9b%e0%b8%84%e0%b8%99%e0%b9%84%e0%b8%9b%e0%b9%80%e0%b8%a2%e0%b9%87%e0%b8%94/', 'https://www.example.com/24992/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2%e0%b9%80%e0%b8%a1%e0%b8%b2%e0%b9%81%e0%b8%a5%e0%b9%89%e0%b8%a7%e0%b9%80%e0%b8%87%e0%b8%b5%e0%b9%88%e0%b8%a2/', 'https://www.example.com/17879/%e0%b8%84%e0%b8%a5%e0%b8%b4%e0%b8%9b%e0%b8%9f%e0%b8%a3%e0%b8%b5%e0%b9%80%e0%b8%94%e0%b9%87%e0%b8%81%e0%b8%aa%e0%b8%b2%e0%b8%a7%e0%b8%a1-%e0%b8%95%e0%b9%89%e0%b8%99%e0%b9%80%e0%b8%87%e0%b8%b5%e0%b9%88/']
# rule = r"[a-zA-Z]+://[^\s]*[$;]"
# for i in testdata:
#     m = re.search(rule ,i)
#     print(m.group().replace("');", ""))

# for data in testdata:
#     da = re.search(r"[a-zA-Z]+://[^\s']*", data)
#     print(da.group(), type(da))


for data in testdata:
    pattern = r"[a-zA-Z]+://+[^\s]+\/[\d]{5,10}\/"
    # da = re.search(pattern, data)
    da = re.findall(pattern, data)
    # print(da)
