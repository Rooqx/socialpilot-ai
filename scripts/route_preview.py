#!/usr/bin/env python3
"""Deterministic offline route preview for integration specifications.
It NEVER invokes an LLM, uses an account, or schedules/publishes content.
Actual AI-agent skill loading and response quality require separate runtime testing.
"""
import argparse, json, re
from pathlib import Path

ROUTES={
 'resume':['social-orchestrator','context-manager'],
 'start':['social-orchestrator','context-manager','voice-profiler'],
 'calendar':['social-orchestrator','editorial-calendar','idea-pipeline'],
 'draft':['social-orchestrator','context-manager','hook-optimizer','fact-checker','copy-editor','post-qa'],
 'thread':['social-orchestrator','x-thread-writer','fact-checker','copy-editor','post-qa'],
 'carousel':['social-orchestrator','carousel-storyboard','visual-brief','instagram-caption-writer','post-qa'],
 'reel':['social-orchestrator','reel-scriptwriter','instagram-caption-writer','post-qa'],
 'repurpose':['social-orchestrator','content-repurposer','platform-strategy','fact-checker','post-qa'],
 'analytics':['social-orchestrator','analytics-and-experiments','continuous-improvement'],
 'listen':['social-orchestrator','social-listening','idea-pipeline'],
 'profile':['social-orchestrator','profile-auditor'],
 'handoff':['social-orchestrator','post-qa','publishing-handoff'],
 'unknown':['social-orchestrator'],
}
WRITERS={'x':'x-post-writer','linkedin':'linkedin-post-writer','instagram':'instagram-caption-writer'}

def plan(user_text, saved_default=None, existing_draft=False):
    s=' '.join(user_text.lower().strip().split())
    platforms=[]
    tests={
      'x':r'\b(?:twitter|tweet|tweets|x post|x posts|x thread|on x|for x)\b',
      'linkedin':r'\b(?:linkedin)\b',
      'instagram':r'\b(?:instagram|insta|ig post|ig carousel)\b',
    }
    for p,pattern in tests.items():
        if re.search(pattern,s):platforms.append(p)
    if not platforms and saved_default in WRITERS:platforms=[saved_default]
    if re.search(r'\b(?:continue|resume|where we stopped|pick up where)\b',s):intent='resume'
    elif re.search(r'\b(?:analy[sz]e|analytics|performance|metrics|insights from my posts)\b',s):intent='analytics'
    elif re.search(r'\b(?:publish|schedule this|post this|send this|share this now|schedule the approved)\b',s):intent='handoff'
    elif re.search(r'\b(?:profile|bio|linkedin headline|optimi[sz]e my account)\b',s):intent='profile'
    elif re.search(r'\b(?:repurpose|adapt this|across platforms|everywhere|turn this into)\b',s):intent='repurpose'
    elif re.search(r'\b(?:start posting|begin posting|get started posting)\b',s):intent='start'
    elif re.search(r'\b(?:this week|next week|calendar|posting plan|weekly posts)\b',s):intent='calendar'
    elif re.search(r'\b(?:reel|reels|short-form video|video script)\b',s):intent='reel'
    elif re.search(r'\b(?:carousel|slides|slide deck)\b',s):intent='carousel'
    elif re.search(r'\b(?:thread|threads)\b',s):intent='thread'
    elif re.search(r'\b(?:listening|mentions|find conversations|monitor our brand)\b',s):intent='listen'
    elif re.search(r'\b(?:post|posts|tweet|caption|write|draft|create)\b',s):intent='draft'
    else:intent='unknown'
    selected=list(ROUTES[intent]); questions=[]
    if intent=='draft' and len(platforms)==1:
        selected.insert(2,WRITERS[platforms[0]])
    elif intent=='draft' and len(platforms)!=1 and not existing_draft:
        questions.append('Which platform should the draft target: X, LinkedIn, or Instagram?')
    if intent=='thread' and platforms and 'x' not in platforms:
        questions.append('Confirm the platform and intended threaded/document format.')
    if intent=='start' and existing_draft:
        selected=['social-orchestrator','context-manager']
    if intent=='draft' and existing_draft:
        return {'intent':'resume_existing_draft','platforms':platforms,'skills':['social-orchestrator','context-manager','post-qa'],'blocking_questions':[],'external_actions_allowed':False,'note':'Prefer existing draft to duplicate generation.'}
    return {'intent':intent,'platforms':platforms,'skills':selected,'blocking_questions':questions,'external_actions_allowed':False,'note':'Offline routing preview only. Not proof of AI runtime routing or post quality.'}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('request')
    parser.add_argument('--default-platform',choices=list(WRITERS))
    parser.add_argument('--existing-draft',action='store_true')
    a=parser.parse_args();print(json.dumps(plan(a.request,a.default_platform,a.existing_draft),indent=2))
if __name__=='__main__':main()
