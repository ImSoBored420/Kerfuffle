list:dict = {
"alaska":"AK",
"alabama":"AL",
"arkansas":"AR",
"arizona":"AZ",
"california":"CA",
"colorado":"CO",
"connecticut":"CT",
"delaware":"DE",
"florida":"FL",
"georgia":"GA",
"hawaii":"HI",
"iowa":"IA",
"idaho":"ID",
"illinois":"IL",
"indiana":"IN",
"kansas":"KS",
"kentucky":"KY",
"louisiana":"LA",
"massachusetts":"MA",
"maryland":"MD",
"maine":"ME",
"michigan":"MI",
"minnesota":"MN",
"missouri":"MO",
"mississippi":"MS",
"montana":"MT",
"north carolina" or "northcarolina":"NC",
"north dakota":"ND",
"nebraska":"NE",
"new hampshire" or "newhampshire":"NH",
"new jersey" or "newjersey":"NJ",
"new mexico" or "newmexico":"NM",
"nevada":"NV",
"new york" or "newyork":"NY",
"ohio":"OH",
"oklahoma":"OK",
"oregon":"OR",
"pennsylvania":"PA",
"rhode island" or "rhodeisland":"RI",
"south carolina" or "southcarolina":"SC",
"south dakota" or "southdakota":"SD",
"tennessee":"TN",
"texas":"TX",
"utah":"UT",
"virginia":"VA",
"vermont":"VT",
"washington":"WA",
"wisconsin":"WI",
"west virginia":"WV",
"wyoming":"WY",
}
def abbreviate_state(output):
        abbreviate = dict.get(f"{output}") 
        return abbreviate

    
