#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Resume PDF File generator
"""

__author__    = 'Jovan Brakus <jovan.brakus@gmail.com>'
__contact__   = 'jovan.brakus@gmail.com'
__date__      = '31 August 2012'

import os
import sys
import traceback
import datetime
import time
import cStringIO

from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas
from reportlab.lib import pagesizes, colors
from reportlab.lib.units import cm, inch
  
RESUME_PAGE_SIZE = pagesizes.letter

#Contants
H_TEXT_MARGIN = 1.3*cm
V_TOP_MARGIN = cm
V_BOTTOM_MARGIN = 0.5*cm

NAME_FONT = "Helvetica-Bold"
NAME_FONT_SIZE = 20

CONTACT_FONT = "Helvetica"
CONTACT_FONT_SIZE = 10

SECTION_V_SPACE = 0.3*cm
SECTION_FONT = "Helvetica-Bold"
SECTION_FONT_SIZE = 12

SUBSECTION_FONT = "Helvetica"
SUBSECTION_TITLE_FONT = "Helvetica-Bold"
SUBSECTION_FONT_SIZE = 10
SUBSECTION_H_INDENT = 0.2*cm
SUBSECTION_V_SPACER = 0.2*cm

H_LINE_MARGIN_OFFSET = 0.3*cm

V_SEPARATOR = 0.1*cm


def _draw_address_lines(canvas, address_lines):
    yc = RESUME_PAGE_SIZE[1] - V_TOP_MARGIN
    canvas.setFont(CONTACT_FONT, CONTACT_FONT_SIZE)
    addr_x = H_TEXT_MARGIN
    
    for address in address_lines:
        addr_y = yc - CONTACT_FONT_SIZE
        canvas.drawString(addr_x, addr_y, address)
        yc = addr_y - V_SEPARATOR
        
    return yc

def _draw_contact_lines(canvas, contact_lines):
    yc = RESUME_PAGE_SIZE[1] - V_TOP_MARGIN
    canvas.setFont(CONTACT_FONT, CONTACT_FONT_SIZE)
    contact_x = RESUME_PAGE_SIZE[0] - H_TEXT_MARGIN
    
    for contact in contact_lines:
        contact_y = yc - CONTACT_FONT_SIZE
        canvas.drawRightString(contact_x, contact_y, contact)
        yc = contact_y - V_SEPARATOR
        
    return yc

def _draw_name(canvas, name):
    yc = RESUME_PAGE_SIZE[1] - V_TOP_MARGIN
    name_x = RESUME_PAGE_SIZE[0] / 2
    name_y = yc - NAME_FONT_SIZE
    
    name = name.upper()
    
    canvas.setFont(NAME_FONT, NAME_FONT_SIZE)
    canvas.drawCentredString(name_x, name_y, name)
    
    return name_y - V_SEPARATOR

def _draw_section_title(canvas, yc, title):
    title = title.upper()
    title_x = H_TEXT_MARGIN
    title_y = yc - SECTION_V_SPACE - SECTION_FONT_SIZE
    line_y = title_y - V_SEPARATOR
    canvas.setFont(SECTION_FONT, SECTION_FONT_SIZE)
    canvas.drawString(title_x, title_y, title)
    canvas.line(H_TEXT_MARGIN - H_LINE_MARGIN_OFFSET, line_y, RESUME_PAGE_SIZE[0] - (H_TEXT_MARGIN - H_LINE_MARGIN_OFFSET), line_y)
    return line_y# - V_SEPARATOR

def _draw_subsection(canvas, yc, title_left, title_middle, title_right, text_tuples):
    if title_left or title_middle or title_right:
        canvas.setFont(SUBSECTION_TITLE_FONT, SUBSECTION_FONT_SIZE)
        title_y = yc - SUBSECTION_FONT_SIZE
        if title_left:
            title_x = H_TEXT_MARGIN
            canvas.drawString(title_x, title_y, title_left)
        if title_middle:
            title_x = RESUME_PAGE_SIZE[0] / 2
            canvas.drawCentredString(title_x, title_y, title_middle)
        if title_right:
            title_x = RESUME_PAGE_SIZE[0] - H_TEXT_MARGIN
            canvas.drawRightString(title_x, title_y, title_right)        
        yc = title_y - V_SEPARATOR
        
    canvas.setFont(SUBSECTION_FONT, SUBSECTION_FONT_SIZE)
    for (draw_bullet, text) in text_tuples:
        if draw_bullet:
            text = u"•  " + unicode(text)
            
        lines = _break_text(text, RESUME_PAGE_SIZE[0] - (2*H_TEXT_MARGIN + SUBSECTION_H_INDENT), SUBSECTION_FONT, SUBSECTION_FONT_SIZE)
        
        line_x = H_TEXT_MARGIN + SUBSECTION_H_INDENT                
        for line in lines:
            line_y = yc - SUBSECTION_FONT_SIZE        
            canvas.drawString(line_x, line_y, line)
            yc = line_y - V_SEPARATOR
    
    return yc - SUBSECTION_V_SPACER
    
def _break_text(text, line_width, font_name, font_size):
    
    space_width = stringWidth(' ', font_name, font_size)
    
    #text = text.decode('utf8')
    delimiter = u' '.decode('utf8')
    words = [word.encode('utf8') for word in text.split(delimiter)]
    
    lines = list()
    line = ''
    available_width = line_width
    while words:
        #Always add first word even if single word is wider than page
        if len(line) == 0:
            line = line + words[0]
            available_width = available_width -  stringWidth(words[0], font_name, font_size)
            del words[0]
        else:
            #We already have at least one word in line. Now we try to add more...
            next_word_width = stringWidth(words[0], font_name, font_size)
            if available_width >= space_width + next_word_width:
                line = line + ' ' + words[0]
                available_width = available_width - (space_width + next_word_width)
                del words[0]
            else:
                #We cannot add more words to current line
                lines.append(line)
                line = ''
                available_width = line_width
    if len(line) > 0:
        lines.append(line)
        
    return lines

def generate_resume(full_name, address_lines, contact_lines, sections):
    """Created Resume PDF Document in memory file (cStringIO object)"""

    pdf_mem_file = cStringIO.StringIO()    
    pdf_canvas = canvas.Canvas(pdf_mem_file, RESUME_PAGE_SIZE)
    
    #Draw header (name, address and contact)
    y1 = _draw_name(pdf_canvas, full_name)
    y2 = _draw_address_lines(pdf_canvas, address_lines)
    y3 = _draw_contact_lines(pdf_canvas, contact_lines)
    
    yc = min([y1, y2, y3])
    
    for (section_name, subsections) in sections:
        yc = _draw_section_title(pdf_canvas, yc, section_name)
        for subsection in subsections:
            yc = _draw_subsection(pdf_canvas, yc, subsection["title_left"], subsection["title_middle"], subsection["title_right"], subsection["text_tuples"])
    
    pdf_canvas.showPage()
    pdf_canvas.save()
    pdf_mem_file.reset()
    pdf_bin_data = pdf_mem_file.read()
    
    return pdf_bin_data
    
def demo():
    """
    Example usage of generate_resume().
    Will writeout resume-demo.pdf into current working dir if file permissions allow
    """
    
    full_name = "Jovan Brakus"
    address_lines = ["My home street #37", "21000 Novi Sad", "Serbia"]
    contact_lines = ["(+381) 63 8102960", "jovan@brakus.rs", "www.brakus.rs"]
    
    employment_sub_emsys_1 = {
        "title_left": "Head of Research&Development",
        "title_middle": "EMSyS Design Inc.",
        "title_right": "September 2012 - ...",
        "text_tuples": [(False, "CellSPY Server Software"),
                        (True, "Responsible for architecture and design of complete CellSPY Server solution. ")]
    }
    employment_sub_emsys_2 = {
        "title_left": "Senior Software Engineer",
        "title_middle": "EMSyS Design Inc.",
        "title_right": "December 2011 - September 2012",
        "text_tuples": [(False, "CellSPY Server Software"),
                        (True, "Implementing complete CellSPY Server software solution. ")]
    }
    employment_sub_dms_1 = {
        "title_left": "Senior Software Engineer",
        "title_middle": "Telvent DMS",
        "title_right": "June 2008 - December 2011",
        "text_tuples": [(False, "Power Management Software"),
                        (True, "Led a team of 4 engineers through architecturing and development phase of Power Management Software solution"),
                        (True, "Project was a layered scada application which relied on Telvent's OASyS Scada infrastructure and implementing power algorithms"),
                        (True, "Power functions implemented: Automatic generation control, Economic Dispatching and Load Predictions"),
                        (True, "Technologies used: Windows, .NET Framework, C++/CLI, C#, Visual Basic, Perl, COM")]
    }
    employment_sub_dms_2 = {
        "title_left": "Software Engineer",
        "title_middle": "Telvent DMS",
        "title_right": "Februar 2007 - June 2008",
        "text_tuples": [(False, "Scada<->DMS Integration component"),
                        (True, "Independently created and implemented dynamical scada data integration component between OASyS DNA Scada and DMS Software"),
                        (True, "Technologies used: Windows, .NET Framework, C++/CLI, C#, COM")]
    }
    education_etf = {
        "title_left": "Belgrade, Serbia",
        "title_middle": "School of Electrical Engineering",
        "title_right": "2001 - 2007",
        "text_tuples": [(True, "Major: Computer Science")]
    }
    education_math = {
        "title_left": "Belgrade, Serbia",
        "title_middle": "Mathematical High School",
        "title_right": "1997 - 2001",
        "text_tuples": [(True, "Mathematical and programming oriented high school. Majors was arithmetics, geometry, physics and programming classes.")]
    }
    education_music = {
        "title_left": "Belgrade, Serbia",
        "title_middle": "Musical High School 'Josip Slavenski'",
        "title_right": "2002 - 2006",
        "text_tuples": [(True, "Major: Opera singing... but really :)")]
    }
    tech_experience = {
        "title_left": "Projects",
        "title_middle": "",
        "title_right": "",
        "text_tuples": [(True, "Srickie: Android game. Available freely on Play Store. www.brakus.rs/srickie"),
                        (True, "ResumeGenerator: PDF Resume generator Web Application (Technologies: ReportLab, Django, AngularJS, Bootstrap). Source: https://github.com/jovanbrakus/resumegen"),
                        (True, "CherryPy-Example: CherryPy Simple demonstration app (Technologies: CherryPy, Jinja2). https://github.com/jovanbrakus/cherrypy-example")]
    }
    additional_experience = {
        "title_left": "",
        "title_middle": "",
        "title_right": "",
        "text_tuples": [(True, "Some awards at Mathematics contest on Country and State levels through Elementary and High School."),
                        (True, "Some awards at Informatics contest on Country and State levels through Elementary and High School."),
                        (True, "Some awards at Opera singing contest on Country and State levels through Elementary and High School.")]
    }
    languages = {
        "title_left": "",
        "title_middle": "",
        "title_right": "",
        "text_tuples": [(True, "C, C++, C#, Python, Perl, JavaScript, ActionScript, SQL"),
                        (True, "Windows, Linux, Visual Studio, Eclipse, Vim")]
    }
    
    sections = [
        ("Employment", [employment_sub_emsys_1, employment_sub_emsys_2, employment_sub_dms_1, employment_sub_dms_2]),
        ("Education", [education_etf, education_math, education_music]),
        ("Technical Experience", [tech_experience]),
        ("Additional Experience and Awards", [additional_experience]),
        ("Languages and Technologies", [languages])]
    
    pdf_bin_data = generate_resume(full_name, address_lines, contact_lines, sections)
    
    pdf_local_file = file('resume-demo.pdf', 'w')
    pdf_local_file.write(pdf_bin_data)
    pdf_local_file.close()    
    
if __name__ == '__main__':
    demo()
    sys.exit(0)