europe = {"spain" : {"capital": "madrid", "pop" : 47},
         "france" : {"capital": "paris", "pop": 67},
         "germany": {"capital" : "berlin", "pop" : 80.83},
        'norway': { 'capital':'oslo', 'pop':5.084 } }

print(europe["france"]["capital"])

data = {"capital": "rome", "pop" :"59.83"}
europe["italy"] = data

print(europe)