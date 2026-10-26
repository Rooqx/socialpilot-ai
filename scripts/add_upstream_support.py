from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
lock=R/'docs'/'source-lock.json'
j=json.loads(lock.read_text());items=j['sources']
commits={'coreyhaines31/marketingskills':'e85f3cbc2e4a79bf33b2a12e9bdd9087d414735b','charlie947/social-media-skills':'10ca79c0ec0be0f7654d19cd4f0c86b6fa6ed23b','blacktwist/social-media-skills':'4f85b07069983b3b0b9bbe6519fed7017edcce81','kostja94/marketing-skills':'b59bbdedd9b203ff731445e37dc11c3a14256547'}
more={
'social':['carousel-frameworks.md','listening.md','listening-sources-template.md','platform-limits.md','platforms.md','post-templates.md','reverse-engineering.md','short-form-video.md','x-algorithm.md'],
'marketing-loops':['loop-catalog.md','loop-guardrails.md','loop-orchestration.md','loop-state.md','loop-template.md'],
'copywriting':['ai-tells.md','copy-frameworks.md','natural-transitions.md'],
'copy-editing':['checklist.md','content-refresh.md','plain-english-alternatives.md'],
'content-strategy':['content-distribution.md','headless-cms.md'],
'customer-research':['source-guides.md','interviews-and-surveys.md'],
'video':['ai-video-prompting.md','edit-anatomy.md','product-demo-recording.md'],
'image':['ai-image-prompting.md'],
'product-marketing':['brand-voice.md'],
'marketing-ideas':['guerrilla-marketing.md','ideas-by-category.md'],
'community-marketing':['community-models.md']}
for skill,files in more.items():
 for f in files:
  repo='coreyhaines31/marketingskills';commit=commits[repo];path=f'skills/{skill}/references/{f}'
  key=(repo,commit,path)
  if any((v['repository'],v['commit'],v['path'])==key for v in items):continue
  items.append({'repository':repo,'commit':commit,'path':path,'url':f'https://github.com/{repo}/blob/{commit}/{path}','referenced_by':[],'source_status':'ADDITIONAL_SPECIALIST_REFERENCE_PINNED_NOT_BUNDLED'})
for path in ['skills/voice-builder/references/sample-content.md','skills/newsletter-voice/references/archetypes.md']:
 repo='charlie947/social-media-skills';c=commits[repo]
 if not any((x['repository'],x['commit'],x['path'])==(repo,c,path) for x in items):
  items.append({'repository':repo,'commit':c,'path':path,'url':f'https://github.com/{repo}/blob/{c}/{path}','referenced_by':[],'source_status':'SUPPLEMENTARY_REFERENCE_NOT_A_USER_WRITING_SAMPLE'})
# Preserve exact source references and avoid supplying upstream author's writing as user biography.
items.sort(key=lambda v:(v['repository'],v['path']))
j['sources']=items
lock.write_text(json.dumps(j,indent=2)+'\n')
print('Source lock expanded:',len(items),'(specialist references included)')
