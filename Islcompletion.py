import os
import re
import sys
import isl
completionList = []

def get_keywords():
    """
    Return the list of keywords from the keyword module available in pypyjs.
    """
    import keyword
    return keyword.kwlist

def get_imported_modules():
    return [m.__name__ for m in sys.modules.values() if m]

def attr_matches(text_comp):
    """
    Compute matches when text contains a dot. This works mostly for chained funciton 
    calls. It splits the text input on the basis of "." , removes the last element that has to be completed
    and then uses dir() to evaluate the type and get the attributes. It is most likely to fail in cases 
    where the "." is used in places different from attributes. 

    Autocompletion functionality is only provided for isl attributes. For instancce, it will provide completions
    for 'isl.m'  but not for any declared variable, class or functions. As the declared variables and
    functions are not statically analysed by the completion module, it will not do autocompletion 
    for them.    
    """
    matches_comp = []
    match_append = matches_comp.append
    m_comp = text_comp.split('=')[-1].strip(' \n\t')
    match_comp = m_comp.split('.')[-1]
    dotlist_comp = m_comp.split('.') 
    n_comp = len(match_comp)
    x_comp = str('.'.join(dotlist_comp[:-1]))
    try:
    	dir(eval(x_comp))
    except Exception:
    	return []
    for word_comp in dir(eval(x_comp)):
      	if word_comp[:n_comp] ==  match_comp:
            match_append(x_comp + "." + word_comp)
    return  matches_comp

def global_matches(text_comp):
    """
    Compute globals matches like keywords, built-in modules, imported modules. Variable completion
    is not supported.
    """
    matches_comp = set()
    match_add = matches_comp.add
    n_comp = len(text_comp)
    for lst_comp in [get_imported_modules(), get_keywords()]:
        if lst_comp is None:
            continue
        for word_comp in lst_comp:
            if word_comp[:n_comp] == text_comp:
                match_add(word_comp)

    return list(matches_comp)

def completions(text_comp):
    """
    Compute the auto-completions for a partial input. It has three part 
    1) import completions(eg "import js" , "from json import json.").
    2) global completions (no "." in the RHS of the expression).
    3) attribute completion("." present in the text).
    """
    if "import " in text_comp:
    	comp_comp = re.split(',|\W', text_comp)[-1]
        if "from " in text_comp:
            imp_module_comp = re.split(',|\W', text_comp)[1]
            completionList = [x_comp for x_comp in dir(eval(imp_module_comp)) if x_comp[:len(comp_comp)] == comp_comp]
            return completionList

        completionList = [x_comp for x_comp in get_imported_modules() if x_comp[:len(comp_comp)] == comp_comp]
        return completionList

    if '.' not in text_comp:
        comp_comp = re.split('\W', text_comp)[-1]
        completionList = global_matches(comp_comp)
        return completionList
    
    completionList = attr_matches(text_comp)
    return completionList

def get_completions():
    """
    Returns the global completion list.
    """
    return completionList
