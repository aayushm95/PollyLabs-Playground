import json

def print_code(ast):
    s = "<pre class='code'><code class=\"cpp hljs\">" + ast.to_C_str() + "</code></pre>"
    print s

def parse_code(code):
    retType = 'string'
    argTypes = ['string']
    args = [code]
    jsn = js.globals.Module.ccall('isclan_get_json', retType, argTypes, args)
    islStringsObj = json.loads(str(jsn))
    context = isl.set(str(islStringsObj["context"]))
    domain = isl.union_set(str(islStringsObj["domain"]))
    schedule = isl.union_map(str(islStringsObj["schedule"]))
    reads = isl.union_map(str(islStringsObj["reads"]))
    writes = isl.union_map(str(islStringsObj["writes"]))
    return (context, domain, schedule, reads, writes)
