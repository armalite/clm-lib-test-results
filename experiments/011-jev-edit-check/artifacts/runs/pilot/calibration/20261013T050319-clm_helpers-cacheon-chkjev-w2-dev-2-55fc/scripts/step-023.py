import json
c=json.load(open('/task/workspace/proposed_context.json'))
for x in c['entries']:
    if x['id']=='sum5': x['body']="Stage 5 (all 5 released): [NEW Record limit] params may contain 'max_records' int>=1; export only first max_records records (ascending id) remaining after every other rule; JSON object key \"truncated\": true if limit left out >=1 record, else false (also when absent). Implemented in core.py just before json.dumps: truncated=False; if max_records not None and len(out)>mr: out=out[:mr]; truncated=True; output keys exported_by, truncated, records. Stage 5 visible tests 2/2 OK (step 22). Remaining: final answer."
json.dump(c,open('/task/workspace/context.json','w'))
print([e['id'] for e in c['entries']])