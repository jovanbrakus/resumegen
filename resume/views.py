import os
import json
import logging 
import sys

from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt                                          

from resume.generator import generate_resume

logger = logging.getLogger(__name__)

def home(request):   
    html_file = open(os.path.join(settings.STATICFILES_DIRS[0], 'index.html'), "r")
    html_raw_content = html_file.read()
    html_file.close()
    return HttpResponse(html_raw_content)

@csrf_exempt
def generate(request):
    try:
        if request.is_ajax():
            if request.method == 'POST':
                resume_json_str = request.POST.get('resume','')
                resumeDict = json.loads(resume_json_str)
                logger.debug("PostData: %s", resume_json_str)
                full_name = resumeDict.get('fullName', '')
                address_lines = resumeDict.get('addressLines','')
                contact_lines = resumeDict.get('contactLines','')
                logger.error("Entering sections")
                sections = []

                for segmentDict in resumeDict.get('lifeSegments', []):
                    segment_title = segmentDict.get('segmentName','')
                    segment_items = []
                    for segItemDict in segmentDict.get('segmentItems',[]):
                        segItem = {}
                        (segItem["title_left"], segItem["title_middle"], segItem["title_right"]) = segItemDict.get('titles', ['','',''])
                        segItem["text_tuples"] = []
                        for lineDict in segItemDict.get('lines',[]):
                            segItem["text_tuples"].append((lineDict.get('drawBullet',True), lineDict.get('lineText','')))
                        segment_items.append(segItem)
                    sections.append((segment_title, segment_items))            
                
                resume_file_data = generate_resume(full_name, address_lines, contact_lines, sections)
                
                response = HttpResponse(resume_file_data, content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename="Resume.pdf"'
                return response
        return home(request)
    except:
        logger.exception("Exception...")
