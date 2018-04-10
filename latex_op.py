def isl_printer_to_str(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_printer_to_str', retType,argTypes, args)

def isl_printer_set_output_format(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_printer_set_output_format',retType, argTypes, args)

def isl_printer_print_set(a_0,a_1):
  retType = 'number'
  argTypes = ['number','number']
  args = [a_0,a_1]
  return js.globals.Module.ccall('isl_printer_print_set',retType, argTypes, args)

def isl_printer_get_str(a_0):
  retType = 'string'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_printer_get_str',retType, argTypes, args)

def isl_printer_free(a_0):
  retType = None
  argTypes= ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_printer_free',retType, argTypes, args)

def isl_printer_print_map(a_0,a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0,a_1]
  return js.globals.Module.ccall('isl_printer_print_map',retType,argTypes,args)

def isl_printer_print_union_map(a_0,a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0,a_1]
  return js.globals.Module.ccall('isl_printer_print_union_map',retType,argTypes,args)

def isl_printer_print_union_set(a_0,a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0,a_1]
  return js.globals.Module.ccall('isl_printer_print_union_set',retType,argTypes,args)

def isl_set_get_latex(s):
  p = isl_printer_to_str(s.ctx.ptr)
  p = isl_printer_set_output_format(p,5)
  p = isl_printer_print_set(p,s.ptr)
  retval = isl_printer_get_str(p)
  isl_printer_free(p)
  return retval

def isl_map_get_latex(m):
  p = isl_printer_to_str(m.ctx.ptr)
  p = isl_printer_set_output_format(p,5)
  p = isl_printer_print_map(p,m.ptr)
  retval = isl_printer_get_str(p)
  isl_printer_free(p)
  return retval

def isl_union_map_get_latex(um):
  p = isl_printer_to_str(um.ctx.ptr)
  p = isl_printer_set_output_format(p,5)
  p = isl_printer_print_union_map(p,um.ptr)
  retval = isl_printer_get_str(p)
  isl_printer_free(p)
  return retval

def isl_union_set_get_latex(us):
  p = isl_printer_to_str(us.ctx.ptr)
  p = isl_printer_set_output_format(p,5)
  p = isl_printer_print_union_set(p,us.ptr)
  retval = isl_printer_get_str(p)
  isl_printer_free(p)
  return retval

def wrap_and_break_lines(string):
  if string.find("\\cup") != -1:
    string = string.replace("\\cup", "\\cup\\\\\\quad\\cup")
    string = string + "\\\\"
    string = "\\begin{array}{l}" + string + "\\end{array}"

  string = "\\[" + string + "\\]"
  return string

def get_latex(latex_ip):
  if isinstance(latex_ip,isl.basic_map):
    y = isl_map_get_latex(isl.map(latex_ip))
  elif isinstance(latex_ip,isl.basic_set):
    y = isl_set_get_latex(isl.set(latex_ip))
  elif isinstance(latex_ip,isl.set):
    y = isl_set_get_latex(latex_ip)
  elif isinstance(latex_ip,isl.map):
    y = isl_map_get_latex(latex_ip)
  elif isinstance(latex_ip,isl.union_map):
    y = isl_union_map_get_latex(latex_ip)
  elif isinstance(latex_ip,isl.union_set):
    y = isl_union_set_get_latex(latex_ip)

  return wrap_and_break_lines(str(y))

def print_latex(latex_ip):
  print(get_latex(latex_ip))
