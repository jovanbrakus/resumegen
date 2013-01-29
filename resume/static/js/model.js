
function Resume(type){
    this.fullName = "";
    this.addressLines = ["","",""];
    this.contactLines = ["","",""];
    this.lifeSegments = new Array();

    this.addSegment = function () {
        this.lifeSegments.push(new LifeSegment());
    }
    this.removeSegment = function (segment) {
        var segIdx = this.lifeSegments.indexOf(segment); // Find the index
        if(segIdx!=-1) this.lifeSegments.splice(segIdx, 1); // Remove it if really found!
    }
}

function LifeSegment(type){
    this.segmentName = "NewSegment";
    this.segmentId = orderNum;
    orderNum = orderNum+1;
    this.segmentItems = new Array();

    this.addSegmentItem = function () {
        this.segmentItems.push(new SegmentItem());
    }

    this.removeSegmentItem = function (segItem) {
        var segItemIdx = this.segmentItems.indexOf(segItem); // Find the index
        if(segItemIdx!=-1) this.segmentItems.splice(segItemIdx, 1); // Remove it if really found!
    }
}

function SegmentItem(type){
    this.titles = ["","",""];
    this.lines = new Array();

    this.addLine = function () {
        this.lines.push(new SegmentPartLine());
    }

    this.removeLine = function (line) {
        var lineIdx = this.lines.indexOf(line); // Find the index
        if(lineIdx!=-1) this.lines.splice(lineIdx, 1); // Remove it if really found!
    }
}

function SegmentPartLine(type){
    this.drawBullet = true;
    this.lineText = "";
}


function PopulateSampleResume(resume){
    resume.fullName = "Jovan Brakus";
    resume.addressLines = ["My home street #37", "21000 Novi Sad", "Serbia"];
    resume.contactLines = ["(+381) 63 8102960", "jovan@brakus.rs", "www.brakus.rs"];
    
    resume.lifeSegments = [];

    resume.addSegment();
    employmentSeg = resume.lifeSegments[0];

    employmentSeg.segmentName = "Employment";
    employmentSeg.addSegmentItem();
    emsysDesign = employmentSeg.segmentItems[0];
    emsysDesign.titles = ["Head of Research&Development", "EMSyS Design Inc.", "September 2012 - ..."];
    emsysDesign.addLine();
    emsysDesign.lines[0].drawBullet = false;
    emsysDesign.lines[0].lineText = "CellSPY Server Software";
    emsysDesign.addLine();
    emsysDesign.lines[1].lineText = "Responsible for architecture and design of complete CellSPY Server solution. ";
    
    employmentSeg.addSegmentItem();
    emsysDesign = employmentSeg.segmentItems[1];
    emsysDesign.titles = ["Senior Software Engineer", "EMSyS Design Inc.", "December 2011 - September 2012"];
    emsysDesign.addLine();
    emsysDesign.lines[0].drawBullet = false;
    emsysDesign.lines[0].lineText = "CellSPY Server Software";
    emsysDesign.addLine();
    emsysDesign.lines[1].lineText = "Implementing complete CellSPY Server software solution";
    
    employmentSeg.addSegmentItem();
    telventDMS = employmentSeg.segmentItems[2];
    telventDMS.titles = ["Senior Software Engineer", "Telvent DMS", "June 2008 - December 2011"];
    telventDMS.addLine();
    telventDMS.lines[0].drawBullet = false;
    telventDMS.lines[0].lineText = "Power Management Software";
    telventDMS.addLine();
    telventDMS.lines[1].lineText = "Led a team of 4 engineers through architecturing and development phase of Power Management Software solution";
    telventDMS.addLine();
    telventDMS.lines[2].lineText = "Project was a layered scada application which relied on Telvent's OASyS Scada infrastructure and implementing power algorithms";
    telventDMS.addLine();
    telventDMS.lines[3].lineText = "Power functions implemented: Automatic generation control, Economic Dispatching and Load Predictions";
    telventDMS.addLine();
    telventDMS.lines[4].lineText = "Technologies used: Windows, .NET Framework, C++/CLI, C#, Visual Basic, Perl, COM";
    
    employmentSeg.addSegmentItem();
    telventDMS = employmentSeg.segmentItems[3];
    telventDMS.titles = ["Software Engineer", "Telvent DMS", "Februar 2007 - June 2008"];
    telventDMS.addLine();
    telventDMS.lines[0].drawBullet = false;
    telventDMS.lines[0].lineText = "Scada<->DMS Integration component";
    telventDMS.addLine();
    telventDMS.lines[1].lineText = "Independently created and implemented dynamical scada data integration component between OASyS DNA Scada and DMS Software";
    telventDMS.addLine();
    telventDMS.lines[2].lineText = "Technologies used: Windows, .NET Framework, C++/CLI, C#, COM";
    
    resume.addSegment();
    educationSeg = resume.lifeSegments[1];

    educationSeg.segmentName = "Education";
    educationSeg.addSegmentItem();
    electricalEngSchool = educationSeg.segmentItems[0];
    electricalEngSchool.titles = ["Belgrade, Serbia", "School of Electricl Engineering", "2001 - 2007"];
    electricalEngSchool.addLine();
    electricalEngSchool.lines[0].lineText = "Major: Computer Science"
    
    educationSeg.addSegmentItem();
    mathHighSchool = educationSeg.segmentItems[1];
    mathHighSchool.titles = ["Belgrade, Serbia", "Mathematical High School", "1997 - 2001"];
    mathHighSchool.addLine();
    mathHighSchool.lines[0].lineText = "Mathematical and programming oriented high school. Majors was arithmetics, geometry, physics and programming classes."
    
    educationSeg.addSegmentItem();
    musicalHighSchool = educationSeg.segmentItems[2];
    musicalHighSchool.titles = ["Belgrade, Serbia", "Musical High School 'Josip Slavenski'", "2002 - 2006"];
    musicalHighSchool.addLine();
    musicalHighSchool.lines[0].lineText = "Major: Opera singing... but really :)"
    
    resume.addSegment();
    experienceSeg = resume.lifeSegments[2];
    experienceSeg.segmentName = "Technical Experience";
    experienceSeg.addSegmentItem();
    projects = experienceSeg.segmentItems[0];
    projects.titles = ["Projects", "",""];
    projects.addLine();
    projects.lines[0].lineText = "Srickie: Android game. www.brakus.rs/srickie";
    projects.addLine();
    projects.lines[1].lineText = "ResumeGenerator: PDF Resume generator Web Application (Technologies: ReportLab, Django, AngularJS, Bootstrap)";
    projects.addLine();
    projects.lines[2].lineText = "CherryPy-Example: CherryPy Simple demonstration app (Technologies: CherryPy, Jinja2). https://github.com/jovanbrakus/cherrypy-example";
    
    resume.addSegment();
    awardsSeg = resume.lifeSegments[3];
    awardsSeg.segmentName = "Additional Experience and Awards";
    awardsSeg.addSegmentItem();
    awards = awardsSeg.segmentItems[0];
    awards.titles = ["", "",""];
    awards.addLine();
    awards.lines[0].lineText = "Some awards at Mathematics contest on Country and State levels through Elementary and High School.";
    awards.addLine();
    awards.lines[1].lineText = "Some awards at Informatics contest on Country and State levels through Elementary and High School.";
    awards.addLine();
    awards.lines[2].lineText = "Some awards at Opera singing contest on Country and State levels through Elementary and High School.";
    
    resume.addSegment();
    languagesSeg = resume.lifeSegments[4];
    languagesSeg.segmentName = "Languages and Technologies";
    languagesSeg.addSegmentItem();
    languages = languagesSeg.segmentItems[0];
    languages.titles = ["", "",""];
    languages.addLine();
    languages.lines[0].lineText = "C, C++, C#, Python, Perl, JavaScript, ActionScript, SQL";
    languages.addLine();
    languages.lines[1].lineText = "Windows, Linux, Visual Studio, Eclipse, Vim";

    
    

}

function PopulateSWEngineeringTemplate(resume){
    resume.fullName = "";
    resume.addressLines = ["", "", ""];
    resume.contactLines = ["", "", ""];
    
    resume.lifeSegments = [];

    resume.addSegment();
    employmentSeg = resume.lifeSegments[0];
    employmentSeg.segmentName = "Employment";
    employmentSeg.addSegmentItem();
    sampleCompany = employmentSeg.segmentItems[0];
    sampleCompany.titles = ["Software Design Engineer", "Microsoft Company", "September 2006 - June 2008"];
    sampleCompany.addLine();
    sampleCompany.lines[0].drawBullet = false;
    sampleCompany.lines[0].lineText = "(Put team of department here) Office Core Team";
    sampleCompany.addLine();
    sampleCompany.lines[1].lineText = "(Add some key points of your work) Implemented UI for some Office subproduct";
    
    resume.addSegment();
    educationSeg = resume.lifeSegments[1];
    educationSeg.segmentName = "Education";
    educationSeg.addSegmentItem();
    university = educationSeg.segmentItems[0];
    university.titles = ["Philadelphia, PA", "University of Pennsiylvania", "2001 - 2006"];
    university.addLine();
    university.lines[0].lineText = "For Example: M.S.E. in Computer and Information Science, September 2006. GPA 4.0"
    
    resume.addSegment();
    experienceSeg = resume.lifeSegments[2];
    experienceSeg.segmentName = "Technical Experience";
    experienceSeg.addSegmentItem();
    projects = experienceSeg.segmentItems[0];
    projects.titles = ["Projects", "",""];
    projects.addLine();
    projects.lines[0].lineText = "Put here your projects. Example TheProjName: Linux Game. source: www.github.com/TheProjName";
    

    resume.addSegment();
    awardsSeg = resume.lifeSegments[3];
    awardsSeg.segmentName = "Additional Experience and Awards";
    awardsSeg.addSegmentItem();
    awards = awardsSeg.segmentItems[0];
    awards.titles = ["", "",""];
    awards.addLine();
    awards.lines[0].lineText = "Put here some awards at any contest...";
    
    resume.addSegment();
    languagesSeg = resume.lifeSegments[4];
    languagesSeg.segmentName = "Languages and Technologies";
    languagesSeg.addSegmentItem();
    languages = languagesSeg.segmentItems[0];
    languages.titles = ["", "",""];
    languages.addLine();
    languages.lines[0].lineText = "C, C++, C#, Python, Perl, JavaScript, ActionScript, SQL";
    languages.addLine();
    languages.lines[1].lineText = "Windows, Linux, Visual Studio, Eclipse, Vim";
}