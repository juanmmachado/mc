
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '\xd7E\x99\xfb\x0e\xe1\xc3\xb0\x1f=\xeeNVr\xfc\xcf'
    
_lr_action_items = {'AND':([7,8,9,10,11,12,13,18,19,20,21,22,],[14,-11,14,14,14,14,14,-10,14,-5,14,14,]),'EVENTUALLY':([0,1,2,3,5,6,14,15,16,17,],[2,2,2,2,2,2,2,2,2,2,]),'RPAREN':([8,9,10,11,12,13,18,19,20,21,22,],[-11,18,-8,-7,-9,-6,-10,-3,-5,-2,-4,]),'NAME':([0,1,2,3,5,6,14,15,16,17,],[8,8,8,8,8,8,8,8,8,8,]),'THEN':([7,8,9,10,11,12,13,18,19,20,21,22,],[15,-11,15,15,15,15,15,-10,15,15,15,15,]),'ALWAYS':([0,1,2,3,5,6,14,15,16,17,],[3,3,3,3,3,3,3,3,3,3,]),'NEXT':([0,1,2,3,5,6,14,15,16,17,],[6,6,6,6,6,6,6,6,6,6,]),'UNTIL':([7,8,9,10,11,12,13,18,19,20,21,22,],[16,-11,16,16,16,-9,16,-10,-3,-5,16,-4,]),'LPAREN':([0,1,2,3,5,6,14,15,16,17,],[1,1,1,1,1,1,1,1,1,1,]),'NOT':([0,1,2,3,5,6,14,15,16,17,],[5,5,5,5,5,5,5,5,5,5,]),'OR':([7,8,9,10,11,12,13,18,19,20,21,22,],[17,-11,17,17,17,17,17,-10,17,-5,17,17,]),'$end':([4,7,8,10,11,12,13,18,19,20,21,22,],[0,-1,-11,-8,-7,-9,-6,-10,-3,-5,-2,-4,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,1,2,3,5,6,14,15,16,17,],[7,9,10,11,12,13,19,20,21,22,]),'statement':([0,],[4,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> expression','statement',1,'p_statement_expr','parserLTL.py',78),
  ('expression -> expression UNTIL expression','expression',3,'p_expression_until','parserLTL.py',82),
  ('expression -> expression AND expression','expression',3,'p_expression_and','parserLTL.py',86),
  ('expression -> expression OR expression','expression',3,'p_expression_or','parserLTL.py',90),
  ('expression -> expression THEN expression','expression',3,'p_expression_then','parserLTL.py',94),
  ('expression -> NEXT expression','expression',2,'p_expression_next','parserLTL.py',99),
  ('expression -> ALWAYS expression','expression',2,'p_expression_always','parserLTL.py',103),
  ('expression -> EVENTUALLY expression','expression',2,'p_expression_eventually','parserLTL.py',107),
  ('expression -> NOT expression','expression',2,'p_expression_not','parserLTL.py',111),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','parserLTL.py',115),
  ('expression -> NAME','expression',1,'p_expression_name','parserLTL.py',123),
]