======================================================================
Chapter 10 Working with File Formats, Security, and Exporting ノート
======================================================================

.. include:: ./common-inc.txt

.. contents:: 章見出し
   :depth: 3
   :local:

File formats
======================================================================

LibreOffice can open a wide variety of file formats as shown below in addition to the Open
Document Format (ODF), including Portable Document Format (PDF).
Most file formats are automatically detected by LibreOffice and can be opened without explicitly
selecting the document format in the file picker.

Text documents
----------------------------------------------------------------------

Writer can read Open Document text formats (.odt, .ott, .oth, .odm, and .fodt), and the following
text formats (including various legacy formats):
Microsoft Word 6.0/95/97/2000/XP/Mac) (.doc and .dot)
Microsoft Word 2003 XML (.xml)
Microsoft Word 2007/2010 XML (.docx, .docm, .dotx, .dotm)
Microsoft WinWord 5 (.doc)
Microsoft Works (.wps)
Abiword Document (.abw, .zabw)
MacWrite Document (.mw, .mcw)
Text CSV (.csv and .txt)
DocBook (.xml)
T602 Document (.602, .txt)
Apple Pages (.pages)
HTML Document (.htm, .html)
WordPerfect Document (.wpd)
Lotus WordPro (.lwp)
ClarisWorks/Appleworks Document (.cwk)
Rich Text Format (.rtf)
StarWriter formats (.sdw, .sgl, .vor)
Unified Office Format text (.uot, .uof)
Hangul WP 97 (.hwp)
eBook (.pdb)
OpenOffice.org 1.x (.sxw, .stw, and .sxg)
When opening .htm or .html files used for web pages, LibreOffice customizes Writer for working
with these files.

Spreadsheets
----------------------------------------------------------------------

Calc can open Open Document spreadsheet formats (.ods, .ots, and .fods) as well as the
following spreadsheet formats (including various legacy formats):
Microsoft Excel 97/2000/XP (.xls, .xlw, and .xlt)
Microsoft Excel 4.x–5.0/95 (.xls, .xlw, and .xlt)
Microsoft Excel 97-2003 (.xml)
Microsoft Excel 2007-365 (.xlsx, .xlsm, .xltx, .xltm)
Microsoft Excel 2007-2010 binary (.xlsb)
Lotus 1-2-3 (.wk1, .wks, and .123)
Data Interchange Format (.dif)
Rich Text Format (.rtf)
Text CSV (.csv and .txt)
StarCalc (.sdc and .vor)
OpenOffice.org 1.x (.sxc and .stc)
dBASE (.dbf)
SYLK (.slk)
Unified Office Format spreadsheet (.uos, .uof)
368 | Chapter 10 Working with File Formats, Security, and Exporting

HTML Document (.htm and .html files, including Web page queries)
Quattro Pro 6.0 (.wb2)
Apple Numbers 2 (.numbers)

Presentations
----------------------------------------------------------------------

Impress can open the various Open Document presentation formats (.odp, .odg, .otp, and .fopd)
as well as the following presentation formats:
Microsoft PowerPoint 97/2000/XP (.ppt and .pot)
Microsoft PowerPoint 2007-365 (.pptx, .pptm, .potx, .potm)
StarDraw and StarImpress (.sda, .sdd, .sdp, and .vor)
OpenOffice.org 1.x (.sxi and .sti)
Unified Office Format presentation (.uop, .uof)
CGM – Computer Graphics Metafile (.cgm)
Portable Document Format (.pdf)
Apple Keynote 5 (.key)

Graphics
----------------------------------------------------------------------

Draw can use the Open Document graphic file formats (.odg and .otg) and PDF files as well as
the following graphic formats:
Adobe Photoshop (*.psd)
AutoCAD Interchange Format (*.dxf)
Corel Draw (*.cdr)
Corel Presentation Exchange (*.cmx)
Microsoft Publisher 98-2010 (*.pub)
Microsoft Visio 2000-2013 (*.vdx; *.vsd; *.vsdm; *.vsdx)
WordPerfect Graphics (*.wpg)
OpenOffice.org 1.x (.sxd and .std)
Bitmap (*.bmp)
Joint Photographic Experts Group (*.jpeg, *.jpg)
Picture Exchange (*.pcx)
Sun Raster (*.ras)
Truevision TGA (*.tga, *.icb, *.vda, *.vst)
Drawing Exchange Format, or Drawing Interchange Format (*.dxf)
eMule Resource Files (*.met)
Portable Gray Map (*.pgm)
Open Office, or Star Office Draw (*.sda)
Tag Image File Format (*.tif, *.tiff)
Windows Metafile (*.wmf)
Enhanced Windows Metafile (*.emf)
Portable Bitmap Image (*.pbm)
Portable Network Graphics (*.png)
StarOffice Presentation (*.sdd)
Encapsulated Postscript (*.eps)
Kodak Photo CD (*.pcd)
Portable Pixmap (*.ppm)
Scalable Vector Graphics (*.svg)
X Window System or X BitMap (*.xbm)
Graphics Interchange Format (*.gif)
Macintosh Picture Image (*.pct)
Photoshop Document (*.psd)
StarView Metafile (*.svm(
X Windows System (*.xpm)

File formats | 369

Formulas
----------------------------------------------------------------------

Math can use Open Document Formula files (.odf) as well as the formats used by OpenOffice.org
1.x (.sxm), StarMath (.smf), and MathML (.mml) files.
When opening a Word document that contains an embedded equation editor object, if the option
MathType to LibreOffice Math or reverse is checked in Tools > Options > Load/Save >
Microsoft Office (macOS LibreOffice > Preferences > Load/Save > Microsoft Office), the
object is automatically converted to a LibreOffice Math object.

File formats for saving
======================================================================

If you save a LibreOffice file in an ODF format, that file will be correctly rendered if it is
transferred to another user, or reopened in a later version of LibreOffice, or opened with another
application that can open ODF files. Thus, we strongly recommend that you save files in an ODF
as file format. However, files can be saved in other formats, if required.

Tip
If the document needs to be shared and it is not going to be modified, the
preferred option is to convert the document to PDF. LibreOffice has an easy
method to convert documents to PDF.

Text documents
----------------------------------------------------------------------

In addition to the ODF text formats (.odt, .ott, and .fodt), Writer can save files in the following
formats:
Office Open XML Text (.docx)
Microsoft Word 2007–365 (.docx, .dotx)
Microsoft Word 97–2003 (.doc)
Microsoft Word 2003 XML (.xml)
Rich Text Format (.rtf)
Text (.txt)
Text Encoded (.txt)
Unified Office Format text (.uot, .uof)
HTML Document (.html and .htm)
DocBook (.xml)

Notes
Since LibreOffice provides encryption support within the Microsoft Word filter,
password protected Microsoft Word documents can be saved.
While the .rtf format is often used to transfer text files between applications, there
is a loss of formatting and images. Thus, users should employ other formats.

Spreadsheets
----------------------------------------------------------------------

Calc can save in the ODF spreadsheet formats (.ods, .ots, and .fods) as well as the following
formats:
Office Open XML Spreadsheet (.xlsx)
Data Interchange Format (.dif)
Microsoft Excel 2007–365 XML (.xlsx)
dBase (.dbf)
Microsoft Excel 97–2003 (.xls and .xlw)
370 | Chapter 10 Working with File Formats, Security, and Exporting

SYLK (.slk)
Microsoft Excel 97–2003 Template (.xlt)
Text CSV (.csv and .txt)
Microsoft Excel 2003 XML (.xml)
Unified Office Format spreadsheet (.uos)
HTML Document (Calc) (.html and .htm)

Presentations
----------------------------------------------------------------------

Impress can save in the ODF presentation formats (.odp, .otp, .fodp, and .odg), as well as the
following formats. Impress can also export to Draw-compatible graphic formats.
Microsoft PowerPoint 2007–365 (.pptx, .potm)
Microsoft PowerPoint 2007–365 AutoPlay (.ppsx)
Microsoft PowerPoint 97–2003 (.ppt)
Microsoft PowerPoint 97–2003 Template (.pot)
Microsoft PowerPoint 97–2003 AutoPlay (.pps)
Office Open XML Presentation (.pptx, .potm, .ppsx)
Unified Office Format presentation (.uop)

Drawings
----------------------------------------------------------------------

Draw can save in the ODF Drawing formats (.odg, .otg, and .fodg) and it can also export to the
graphics formats BMP, EMF, EPS, GIF, JPEG, PNG, SVG, TIFF, and WMF.

Writer/Web documents
----------------------------------------------------------------------

Writer/Web can save to the following formats:
HTML document (.html and .htm), as HTML 4.0 Transitional
Text and Text Encoded (LibreOffice Writer/Web) (.txt)

Exporting files
======================================================================

LibreOffice uses the term “export” for file operations where there is a change of file type. Unlike
Save As, exporting the file produces a document while keeping the current file format of the
actual document. If the file type cannot be found in File > Save As on the Menu bar, check File >
Export on the Menu bar (not available in Math) for additional file types.
If the PDF file format is needed, LibreOffice can export Writer, Calc, Impress, and Draw,
documents in that format. Writer can also export in EPUB. Also, LibreOffice can export files in
HTML and XHTML formats. Draw and Impress can also export in several image and graphic
formats.

Note
If you use the Export command, LibreOffice will create a copy of the file as a new
file using the selected format. The original file will remain open in LibreOffice.

Exporting files | 371

Figure 311: Export dialog

PDF quick export
----------------------------------------------------------------------

If a file needs to be quickly exported to the PDF format, LibreOffice is unable to select various file
options such as file format, page range, and image compression. For a quick PDF export, do the
following:
1)

Open the target file in LibreOffice.

2)

Open the Export dialog (Figure 311) and use one of the following methods:
– Click on Export Directly as PDF on the Standard toolbar.
– Go to File > Export As > Export Directly as PDF on the Menu bar.

3)

Enter a file name and select the required location for the PDF file in the Export dialog.

4)

Click on Export to create the PDF file and close the Export dialog.

Note
By default, a file in PDF format is not protected against contents tampering, or
editing. Contents of a PDF file can be edited by specialized software tools,
including LibreOffice Draw.

Controlled PDF export
----------------------------------------------------------------------

If you need more control over the content and quality of a file that will be exported in the PDF
format, do the following in the PDF Options dialog (Figure 312):
1)

Open the target file in LibreOffice.

2)

Access PDF Options by going to File > Export As > Export as PDF.

372 | Chapter 10 Working with File Formats, Security, and Exporting

Figure 312: PDF Options dialog — General page
3)

Select the various options required on each tabbed page of the PDF Options dialog.

4)

Click on Export to open the Export dialog.

5)

Navigate to the required folder for the PDF file.

6)

Enter a file name the PDF file and click on Export to save the PDF file in its selected
location.

General PDF options
Refer to Figure 312 to see the PDF options available on the General page of the PDF dialog.
Range
Sets the export options for the pages included in a PDF file.
All
Exports all defined print ranges. If no print range is defined, the entire document will be
exported.
Pages
Exports the pages that you have selected. To export a range of pages, use the format
3-6. To export single pages, use the format 7;9;11. If you want, you can export a
combination of page ranges and single pages, by using a format like 3-6;8;10;12.
Selection
Exports all the current selection.
View PDF after export
Opens the exported PDF file in the default PDF viewer application.
Images
Sets the PDF export options for images in a PDF file.

Exporting files | 373

Lossless compression
Selects lossless compression for the image. All pixels are preserved. This setting can
create large files when used with photographs.
JPEG compression quality
Determine the JPEG compression’s quality level. Almost all pixels are preserved if you
choose a high quality level, but if you use a low quality level, file sizes are reduced but
some pixels are lost and artifacts are introduced.
Reduce image resolution
Lower DPI (dots per inch) images have lower quality. Lower resolutions (100 DPI or
less) may be sufficient for viewing on a computer screen, but many modern devices
have much higher resolutions. For printing it is generally preferable to use at least 300
or 600 DPI, depending on the capability of the printer. Higher DPI settings increase the
size of the exported file.

Note
Encapsulated PostScript (EPS) images with embedded previews are exported
only as previews. EPS images without embedded previews are exported as
empty placeholders.
Watermark
Add a centered, vertical, light green watermark text to the page background. The
watermark is not part of the source document.
Sign with watermark
Insert the required text for the watermark signature. When this option is selected, a
watermark signature appears on the PDF pages.
General
Sets general PDF export options.
Hybrid PDF (embed ODF file)
Use this setting to export the document with a hybrid file format: PDF and ODF. In PDF
viewers it behaves like a normal PDF file, but remains fully editable in LibreOffice.
Archive (PDF/A, ISO 19005)
Converts to the PDF/A-1b, PDF/A-2b, or PDF/A-3b format. All fonts used in the source
document are embedded in the generated PDF file, and PDF tags are created. The
primary purpose is to create an electronic document whose appearance is independent
of device and application, making it suitable for long term preservation.
PDF/A-2b is recommended for most users, because it allows for layers and
transparency with shapes and images. It also compresses better (JPEG 2000) than
PDF/A-1b, usually producing smaller files. PDF/A-3b is identical to PDF/A-2b, but also
accepts embedding of other file formats.
Universal Accessibility (PDF/UA)
Creates a universal, accessible PDF file that follows the requirements of PDF/UA (ISO
14289) specifications.
Tagged PDF (add document structure)
Tagged PDFs contain information about the structure of document contents. This can
help to display the document on devices with different screens and using screen reader
applications. Some tags that are exported are table of contents, hyperlinks, and
controls. This option can increase file sizes significantly.

374 | Chapter 10 Working with File Formats, Security, and Exporting

Create PDF form
If you are submitting forms within the PDF file, select the available options fromthe
Submit format drop-down list. This menu will override the URL property that is set in the
document. Only one setting is valid for the PDF document: PDF (sends the whole
document); FDF (sends the control contents); HTML, and XML. Normally PDF format is
selected.
Allow duplicate field names
Allows the use of the same field name for multiple fields in a generated PDF file. If
disabled, field names are assigned generated unique names.
Structure
Sets options for diverse features such as bookmarks, comments, page layout, and so on.
Export outlines
Use this option to export bookmarks of Writer documents as PDF bookmarks.
Bookmarks are created for all outline paragraphs and for all table of contents entries
where hyperlinks are assigned in the source document.
Only paragraphs with Outline level 1 — 10 are exported. The name of the Paragraph
Style is irrelevant. For example, the default version of Paragraph Style Title is not
exported when its Outline level is Text Body.
Export placeholders
This option is only available in Writer. The user can choose if the PDF file will include
any defined placeholder fields, which can be filled in by users.
Comments as PDF annotations
If this option is selected, comments are included in the PDF file as annotations.
To export comments of Writer documents as displayed in LibreOffice, select Tools >
Options > LibreOffice Writer > Print (macOS LibreOffice > Preferences >
LibreOffice Writer > Print) and select the In margins option in Comments. The
exported pages are scaled down and the comments are placed into margins.
Export automatically inserted blank pages
If selected, blank pages are automatically inserted in the PDF file. This is
recommended if you are printing the PDF file as a double-sided document. For
example, books usually have chapters set to start on an odd-numbered (right-hand)
page. When the previous chapter ends on an odd page, LibreOffice inserts a blank
page between the two odd pages. This option controls whether to export that blank
page.
Use reference Xobjects
This option determines how PDF images will be exported back into a PDF file.
When this option is disabled, the first page of the PDF data is included in the output.
The PDF export merges images, fonts and other resources during export. This is a
complex operation, but the result can be viewed in various viewers.
If this option is enabled, the reference XObject markup is used. This is a simple
operation, but PDF viewers must support this to use vector images. Otherwise, a
fallback bitmap is shown in the viewer.
More information can be found in the PDF specification, ISO 32000-2:2017
(https://www.iso.org/standard/63534.html).

Exporting files | 375

Figure 313: PDF Options dialog — Initial View page

Initial View PDF options
The Initial View page in the PDF Options dialog (Figure 313) allows users to determine how the
PDF file opens by default in a PDF viewer.
Panes
Page only
Generate a PDF file that shows only page contents.
Outline and page
Generate a PDF file that shows a bookmarks palette and page contents.
Thumbnails and page
Generate a PDF file that shows a thumbnails palette and the page contents.
Open on page
Enter a page number to display that page when a PDF reader opens a PDF file.
Magnification
Default
Generate a PDF file that shows the page contents without zooming. If the PDF reader
application is configured to use a zoom factor by default, the page displays with that
zoom factor.
Fit in window
Generate a PDF file that displays the page zoomed to fit entirely into a PDF reader
window.
Fit width
Generate a PDF file that displays the page zoomed to fit the width of a PDF reader
window.
Fit visible
Generate a PDF file that displays the text and graphics on the page zoomed to fit the
width of a PDF reader window.
Zoom factor
Enter a zoom factor which determines when a PDF reader opens a PDF file.

376 | Chapter 10 Working with File Formats, Security, and Exporting

Page layout
Default
Generate a PDF file that displays the pages according to the layout setting of the PDF
reader application.
Single page
Generate a PDF file that displays one page at a time.
Continuous
Generate a PDF file that displays pages in a continuous vertical column.
Continuous facing
Generate a PDF file that displays pages side by side in a continuous column. For more
than two pages, the first page is displayed on the right.
First page is left
Generate a PDF file that shows pages side by side in a continuous column. For more
than two pages, the first page is displayed on the left. Complex Text Layout must be
enabled in Tools > Options > Language Settings > Languages (macOS LibreOffice
> Preferences Language Settings > Languages) for this option to be available.

User Interface PDF options
The User Interface page in the PDF Options dialog (Figure 314), allows users to specify how the
interface for an external PDF viewer will appear. If you need to create a PDF file that will be used
as a presentation or a kiosk-type display, these options are useful.
Window Options
Resize window to initial page
Generate a PDF file that is shown in a window displaying the whole initial page.
Center window on screen
Generate a PDF file that is shown in a PDF reader application that is centered on the
display.
Open in full screen mode
Generate a PDF file that is shown in full screen in a PDF reader window and in front of
all other windows.
Display document title
Generate a PDF file that will display the file title in the PDF reader’s title bar.

Figure 314: PDF Options dialog — User Interface page
User Interface Options
Hide menubar
Hide the menu bar when a PDF file is active.

Exporting files | 377

Hide toolbar
Hides the toolbar when a PDF file is active.
Hide window controls
Hides the reader controls when a PDF file is active.
Transitions
Use transition effects
Exports Impress slide transition effects to respective PDF effects.
Collapse Outlines
Show All
Select to show all outline levels as bookmarks when a PDF reader opens a PDF file.
Visible levels
Select to show bookmarks down to the selected level when a PDF reader opens a PDF
file.

Links PDF options
The PDF Options dialog Links page (Figure 315) specifies how outlines and hyperlinks will be
exported in a document.
General
Export outlines as named destinations
The bookmarks (targets of references) in PDF files are defined as rectangular areas.
Additionally, bookmarks to named objects are defined by their names. A checkbox can
allow you to export the names of objects in a document as valid bookmark targets. This
allows objects to be exported by name from other documents.
Convert document references to PDF targets
This option automatically converts filename extensions in URLs from ODF to PDF. In
the referencing URLs, the extensions .odt, .odp, .ods, .odg, and .odm are converted to
the extension .pdf.
Export URLs relative to file system
This option allows URLs to be exported to other documents as relative URLs in the file
system.
Cross-document links
Specify how to handle hyperlinks from a PDF file to other files.

Figure 315: PDF Options dialog — Links page
Default mode
All links from a PDF document to other documents are handled as specified in the
computer operating system.

378 | Chapter 10 Working with File Formats, Security, and Exporting

Open with PDF reader application
Cross-document links are opened with the PDF reader application that currently shows
the document. The PDF reader application must be able to handle the specified file
type inside the hyperlink.
Open with Internet browser
Cross-document links are opened with a web browser. The web browser must be able
to handle the specified file type inside the hyperlink.

Security PDF options
The Security page in the PDF Options dialog (Figure 316) specifies the security options used by
an exported PDF file.

Note
The document permission restrictions set by a password are observed only by
PDF readers compliant with the version 1.5 of the PDF format. For older PDF
readers, these restrictions may have no effect.
File Encryption and Permission
Set passwords
Opens a dialog box where passwords are entered. Specify a password required for
viewing a PDF file. Enter an optional password that allows a user viewing the PDF to
edit and/or print the document.
Printing
Not permitted
Users will not be able to print the document.
Low resolution (150 dpi)
The document can only be printed in low resolution (150 dpi). However, some PDF
readers ignore this option.

Figure 316: PDF Options dialog — Security page
High resolution
The document can be printed in high resolution.

Exporting files | 379

Changes
Not permitted
The content of the PDF file cannot be changed.
Inserting, deleting, and rotating pages
Inserting, deleting, and rotating pages will be permitted.
Filling in form fields
Filling in form fields is permitted.
Commenting, filling in form fields
Only commenting and filling in form fields is permitted.
Any except extracting pages
All changes are permitted, except extracting pages.
Contents
Enable copying of content
Content can be copied to the clipboard.
Enable text access for accessibility tools
Select to enable text access for accessibility tools.

Digital Signature PDF options
The PDF Options dialog’s Digital Signatures page in Figure 317 specifies how the exported
PDF file can be digitally signed.
•

Digital signatures are used to ensure that the PDF was really created by the original
author and that the document has not been modified since it was signed.

•

The signed PDF export uses the keys and X.509 certificates already stored in a default
key store location, or on a smart card.

•

When using a smart card, it must already be configured for use by a key store. This is
usually done during installation of smart card software.

Certificate
Use this certificate to digitally sign PDF documents
Allows users to select a certificate to be used for signing a PDF export.
Select
Opens the Select Certificate dialog.
All certificates found in the selected key store are displayed. If the key store is
protected by a password, there is a prompt to enter a password. When using a smart
card that is protected by a PIN, there is a prompt to enter the PIN.
Select the certificate to use for digitally signing the exported PDF by clicking on the
corresponding line, then click OK.
All other fields on the Digital Signatures page are only accessible after a certificate has
been selected.
Certificate password
Enter the password that will be used to protecting the private key associated with the
selected certificate. Usually this is the key store password.

380 | Chapter 10 Working with File Formats, Security, and Exporting

Figure 317: PDF Options dialog — Digital Signatures page

Notes
If the key store password has already been entered in the Select Certificate
dialog box, the key store may already be unlocked and not require the password
again. But to be on the safe side, enter the password.
When using a smart card, enter the PIN here. Some smart card software prompts
you to enter the PIN again before signing.
Location, Contact information, Reason
These three fields allow additional information to be entered about the digital signature
that is applied to the PDF (where, by whom and why it was made). It is embedded in
the appropriate PDF fields and is visible to anyone viewing the PDF. Each, or all of the
three fields, are optional and may be left blank.
Time Stamp Authority
The PDF signing process uses the Time Stamp Authority (TSA) to obtain a digitally
signed timestamp that is then embedded in the signature. This (RFC 3161) timestamp
allows viewing of the PDF to verify when the document was signed.
If no TSA URL is selected (the default), the signature is timestamped, but it uses the
current time from the local computer.

EPUB format export (Writer only)
======================================================================

EPUB is standard for electronic book files with the extension .epub that can be downloaded and
read on devices like smartphones, tablets, computers or e-readers. The EPUB format is
implemented as an archive file consisting of HTML files carrying the content, along with images
and other supporting files.
Writer can export a file to EPUB. A text-only document generally exports well, but some contents
(such as illustrations, tables, and cross-references) may not export correctly.

Quick EPUB export
----------------------------------------------------------------------

If you choose to quickly export a Writer file to the EPUB file format, there is no control over
content and quality of the EPUB file.
1)

Open the Writer file that is going to be converted.

EPUB format export (Writer only) | 381

2)

Go to File > Export As > Export Directly as EPUB on the Menu bar and the Export
dialog opens.

3)

Navigate to the folder where the EPUB file is going to be saved.

4)

Enter a file name in the File name text box. The format of the exported file is fixed to
EPUB Document (.epub).

5)

Click on Export and the Writer file is converted to an EPUB file and saved in the selected
location.

Controlled EPUB export
----------------------------------------------------------------------

To control the content and quality of the resulting EPUB file in Writer, do the following:
1)

Open the Writer file that is going to be converted.

2)

Go to File > Export As > Export as EPUB and open the EPUB Export dialog
(Figure 318).

3)

Enter the necessary information into the various options in EPUB Export dialog. For more
information, refer to “EPUB export options” below.

4)

Click OK to close the EPUB Export dialog and open the Export dialog.

5)

Navigate to the folder where the EPUB file is going to be saved.

6)

Enter a file name in the File name text box. The format of the exported file is fixed to
EPUB Document (.epub).

7)

Click on Export and the Writer file is converted to an EPUB file and saved in the selected
location.

Tip
Other ways to export to EPUB from Writer (.odt) files include Calibre, an open
source e-book manager that runs on Windows, macOS, and Linux. Calibre
provides many e-book conversion facilities (including PDF to EPUB) and allows
editing of the conversion. See https://calibre-ebook.com/ for more information.

EPUB export options
----------------------------------------------------------------------

General
Version
Sets the version of the resulting EPUB file.
Split method
Select the type of start of the next EPUB section.
Heading — Starts the next section on headings, according to the document outline
numbering.
Page break — Starts the new section on a page break.
Layout method
Determines the layout that is generated for the EPUB document.
Reflowable — Content flows (or reflows) to fit the screen and to fit the needs of the
user. This also means that page style information (for example, page size or
header/footer content) will not be exported.
Fixed — Gives greater control over presentation when a reflowable EPUB is not
suitable for its content.

382 | Chapter 10 Working with File Formats, Security, and Exporting

Figure 318: EPUB Export dialog
Customize
Custom cover image
Enter the full path of the custom cover image file. If the entry is empty, the exporter
uses the cover image in the media directory when the name is one of the following:
cover.gif, cover.jpg, cover.png, or cover.svg. The custom cover image is
embedded in the EPUB file.
Custom media directory
Enter the custom media directory for the EPUB file. The media directory may contain a
cover image as seen above, custom metadata and image links.
By default, the exporter looks inside a folder in the current document directory with the
same name of the document file name for custom media and custom metadata. For
example, if the document name is MyText.odt, the default media folder for cover and
metadata is MyText in the current directory.
For custom metadata, provide a file with same name as the original filename with the
extension .xmp. The provided metadata overrides the internal document metadata. In
the example above, the custom metadata must exist in the MyText directory as
MyText.xmp.

Image links mean that if create relative links are created on images or text and they link
an image that is available in the media directory, then this media is available in the
EPUB export file as a pop-up.
Metadata
Enter the custom metadata that overrides the document default metadata. These text
fields can be left empty.
Identifier
Enter a unique identifier for the publication.

EPUB format export (Writer only) | 383

Title
Enter the title of the publication.
Author
Enter the Author of the publication.
Language
Language of the publication (see RFC4646 and ISO 639 for possible values).
Date
Last modification date for the publication. The value of this property must be an XML
Schema date Time conformant date in the form: CCYY-MM-DDThh:mm:ssZ. Default is
the date and time when the export dialogue box opened.

Creating HTML files
======================================================================

The easiest way to create HTML documents in LibreOffice is to start with an existing text
document. For example, in Writer, go to View > Web and the view will change to show how the
text document appears as a web page. However, Web view does not show which features will, or
will not be saved correctly in HTML format. Refer to “HTML files using Writer/Web” on page 443
for more information on creating a web page from a text document.

Text documents
----------------------------------------------------------------------

Note
The use of styles in the text document is strongly recommended when saving, or
exporting to HTML, or XHTML format.
Saving a text document as HTML is limited by the HTML 4.0 Transitional
specification. Text documents in office suites normally use a richer set of
resources that do not appear in HTML, for example page formatting. Do not
expect the same layout when saving a file in HTML format.

Saving as HTML
A text document can be saved in HTML format so that it can be viewed in a web browser. To
generate a separate HTML page, you can associate a page break with a specific heading
paragraph style each time that style appears in the document. The Writer module automatically
creates a page containing hyperlinks to each of these pages.
When you save a text document in HTML format, any graphics in the document are saved into
the HTML document as embedded data streams. For graphics, JPEG, or SVG formats are saved
as HTML and all other graphic formats are saved as PNG.
LibreOffice generates the image files and the HTML file necessary to create an HTML page in a
browser. The number of files generated by the format conversion depends on the number of
images and objects in the original text document. Refer to Table 11 for the file types created and
file content when saving HTML format.
Table 11: File types created saving in HTML format
File
Myfile.html
Myfile_html_[random number].gif
Myfile_html_[random number].png,
jpg, or bmp

Contents
The text contents, page layout, text attributes, meta
tags, and styles.
GIF images of visible contents of OLE objects.
Images inserted in the text document as PNG, BMP, or
JPEG keep their original format.

384 | Chapter 10 Working with File Formats, Security, and Exporting

To create a HTML file from a text document, do the following:
1)

Create a new folder which will be a location for the HTML file and images.

2)

To open the Save As dialog, select File > Save As on the Menu bar.

3)

Navigate to the required location in the Save As dialog.

4)

Enter a file name for the HTML file in the File name: text box.

5)

In File type:, select HTML Document (Writer) (.html) as the file type.

6)

Click on Save to save the file as HTML and close the Save As dialog.

7)

If necessary, click on Use HTML Document (Writer) Format in the Confirmation dialog
that opens confirming the file is saved as HTML.

Export as XHTML
If you want LibreOffice to export a text document as a XHTML file, LibreOffice generates an
XHTML file for each text document. Image files are also embedded in the XHTML file.
LibreOffice-generated XHTML files have better layout rendering, but fail to render objects other
than images.
1)

If necessary, create a new folder as a location for the HTML file and images.

2)

Go to File > Export on the Menu bar to open the Export dialog (Figure 311 on page 423).

3)

Navigate to the location of the new folder in the Export dialog.

4)

Enter a file name for the HTML file in the File name: text box.

5)

In File type:, select XHTML (Extensible Hypertext Markup Language) as the file type.

6)

Click on Export to save the file as XHTML and close the Export dialog.

Notes
Writer does not replace multiple spaces in the original document with the HTML
code for non-breaking spaces. To create extra spaces in a HTML file or web
page, insert non-breaking spaces in LibreOffice. To enter non-breaking spaces,
use the keyboard shortcut Ctrl+Spacebar (macOS ⌘+Shift+Spacebar).
The Tab character is not rendered when LibreOffice exports to XHTML. Instead,
use borderless tables to position contents instead of the Tab character in a line.
You will have to change the bullet and number lists that insert a Tab character
between the bullet or number and the text—instead, create a list style where the
Tab character is replaced by a space.
Objects that are different from usual image formats are not rendered in
LibreOffice XHTML output. This includes drawings, spreadsheets, charts, and
OLE objects in general. To render an OLE object in XHTML, replace the
document’s OLE object with an image of the OLE object.

Saving document as a series of web pages
Writer can save a large document as a series of web pages (HTML files) with a table of contents
page. To this, follow these steps:
1)

Decide which heading style in a document starts a new page and make sure all those
headings have the same paragraph style, for example, Heading 1.

2)

Go to File > Send > Create HTML Document on the Menu bar and open the Name and
Path of the HTML Document dialog (Figure 319).

Creating HTML files | 385

Figure 319: Name and Path of the HTML Document dialog
3)

Navigate to the place where the HTML file is going to be saved.

4)

Enter a file name in the File name: text box.

5)

Select HTML Document from options available from the File type:.

6)

In separated by:, select the style from the drop-down list that is going to create a new
page in the HTML file, for example Heading 1.

7)

Click on Save to create the multi-page HTML document and close the dialog. The HTML
files created conform to the HTML 4.0 Transitional standard.

Spreadsheets
----------------------------------------------------------------------

Calc can save spreadsheet files as HTML documents. If the file contains more than one sheet,
the additional sheets follow each other in the HTML file. Links to each sheet are placed at the top
of the HTML document. To do this task, perform the following steps:
1)

If necessary, create a new folder as a location for the HTML file.

2)

Open the Save As dialog by selecting File > Save As on the Menu bar.

3)

Navigate to the required location in the Save As dialog.

4)

Enter a file name for the HTML file in the File name: text box.

5)

Select HTML Document (Calc) (.html) in the File type: field.

6)

Click on Save to save the file as HTML and close the Save As dialog.

7)

If necessary, click on Use HTML Document (Calc) Format in the Confirmation dialog
that opens confirming the file is saved as HTML.

386 | Chapter 10 Working with File Formats, Security, and Exporting

Note
Calc allows the insertion of links directly into a spreadsheet using the Hyperlink
dialog. See Chapter 4, Working with Styles, Templates and Hyperlinks, for more
information on hyperlinks.

Presentations and drawings
----------------------------------------------------------------------

Exporting
Impress presentations and Draw drawings cannot be saved in HTML format, but can be exported
as HTML documents in the HTML Export dialog.

Notes
When you save Impress presentations in HTML format, the new HTML file does
not retain any animation or any slide transitions that have been created in the
Impress presentation.
Click on Create on the HTML Export dialog at any stage in the following
procedure to create the HTML file. If a web page design has not been previously
created, the option Existing design is not available on the Assign Design page of
the HTML Export dialog.
Depending on the size of a presentation, or drawing and the number of graphics it
contains, the HTML export function will create several HTML, JPG, and GIF files.
You should create a folder to hold all the files needed for the web version of a
presentation, or drawing. Saving to the desktop and not to a specific folder, the
HTML and graphics files are placed onto the desktop, which could create
difficulties in locating the files.
1)

If necessary, create a new folder as a location for the HTML file.

2)

Go to File > Export on the Menu bar to open the Export dialog (Figure 311 on page 423).

3)

Navigate to the location of the new folder in the Export dialog.

4)

Enter a file name for the HTML file in the File name: text box.

5)

Select HTML Document (Impress) (.html; .htm), or HTML Document (Draw)
(.html; .htm) from the In File type: drop-down menu.

6)

Click on Export to open the HTML Export dialog (Figure 320).

7)

Select the required option, or enter the necessary information on each page of the HTML
Export dialog, then click on Next to open the next page in the HTML Export dialog. See
“HTML options” below for more information on available options.

8)

When the HTML design is completed to your requirements, click on Create to close the
HTML Export dialog and create the HTML file.

HTML options
Assign Design
Refer to Figure 320. This page allows you to create a new design, select an existing
design, or delete an existing design. If a design is deleted, only the design information is
deleted in the Export dialog. An export file will not be deleted by this action.
New design
Creates a new design using the pages of the Export dialog.

Creating HTML files | 387

Figure 320: HTML Export dialog — Assign Design page

Figure 321: HTML Export dialog — Publication Type page
Existing Design
Loads an existing design from the design list displayed. This will used as a starting point
in creating a HTML design.
Delete Selected Design
Deletes the selected design from the design list. Only available when an existing design is
selected.
Publication type
Refer to Figure 321. This defines the basic settings for exporting the HTML file.
Standard HTML format
Creates standard HTML pages from export pages.
Standard HTML with frames
Creates standard HTML pages with frames. The exported page is placed in the main
frame. The frame to the left displays a table of contents in using hyperlinks.

388 | Chapter 10 Working with File Formats, Security, and Exporting

Single-document HTML
Creates a single file containing the text of the presentation, but not the layout, or
images.
Automatic
Creates a default HTML presentation as a kiosk export, where pages are automatically
advanced after a specified amount of time and does not depend on the document
contents.
WebCast
In a WebCast export, automatic scripts are generated with Perl or ASP support. This
enables the speaker (for example, a speaker in a telephone conference using a slide
show on the Internet) to change pages in web browsers used by the audience. more
information on WebCast is available on the LibreOffice help pages.
Options
Refer to Figure 321.
Create title page
Creates a title page for a document.
Show notes
Specifies that notes are also displayed.
Save images as
Refer to Figure 322. Determines the image format and defines the compression value for
export.
PNG
Export images into the Portable Network Graphics (PNG) format. PNG files are
compressed without loss of data, and can contain more than 256 colors.
GIF
Export images into the Graphics Interchange Format (GIF). GIF files are compressed
without loss of data, and have a maximum of 256 colors.

Figure 322: HTML Export dialog — Save images as page
JPG
The files are exported into the Joint Photographic Experts Group (JPEG) format. JPEG
files have adjustable compression and can contain more than 256 colors.
Quality
Specifies the compression factor used when files are exported into the JPEG format. A
100% value offers the best quality for a large data range. A 25% factor indicates small
files with inferior image quality.

Creating HTML files | 389

Effects
Refer to Figure 322.
Export sounds when slide advances
Specifies that the sound files that are defined as a transition effect are exported.
Export hidden slides
Exports any hidden slides in a presentation.
Monitor resolution
Refer to Figure 322. Defines the resolution for the target screen. Depending on the
selected resolution, the image may be displayed in a reduced size. A reduction of up to
80% from the original size can be specified.
Low (640 × 480 pixels)
Select low resolution to keep the file size small, even for presentations with many
slides.
Medium (800 × 600 pixels)
Select medium resolution for a medium-sized presentation.
High (1024 × 768 pixels)
Select high resolution for a high quality display.
Full HD (1920 × 1080 pixels)
Select high definition resolution for a high quality display.
Information for the title page
Refer to Figure 323.
Author
Contains the name of the author.

Figure 323: HTML Export dialog — Title page

390 | Chapter 10 Working with File Formats, Security, and Exporting

Figure 324: HTML Export dialog — Button page
Email address
Contains the email address of the author
Your homepage
Contains the homepage of the author. A hyperlink is inserted in the HTML file.
Additional information
Contains any additional text required for the title page.
Select button style
Refer to Figure 324. Specifies the style of navigation buttons used in the presentation.
Text only
Inserts only text hyperlinks instead of buttons.
Selection box
Displays the available button styles. Click on a button style to select it.
Select color scheme
Refer to Figure 325. Determines the color scheme and the colors for text and
background.
Apply color scheme from document
Determines the colors from the styles used in the current document.
Use browser colors
Uses the default colors of a web browser.
Use custom color scheme
Allows definition of custom colors for some presentation objects.
Text
Select colors for the text in the presentation.
Hyperlink
Select colors for the presentation’s hyperlinks.
Active Link
Select colors for the presentation’s active links.

Creating HTML files | 391

Figure 325: HTML Export dialog — Color Scheme page
Visited Link
Select colors for the presentation’s visited links.
Background
Select the presentation’s background color.

HTML files using Writer/Web
LibreOffice Writer has a configuration called Writer/Web that can create, edit, and save files in
HTML format. Writer/Web is only available when working with documents that are in HTML
format.

Display modes
----------------------------------------------------------------------

By default, Writer/Web opens an HTML file in Normal view (Figure 326). To change Writer/Web
to Web view, go to View > Web on the Menu bar (Figure 327). If necessary, Normal or Web view
are used to add to an HTML document, then edit and format the contents of the HTML document.
The contents in an HTML document are rendered as if displayed in a browser.

Figure 326: Example of Normal view in Writer/Web

392 | Chapter 10 Working with File Formats, Security, and Exporting

Figure 327: Example of Web view in Writer/Web

Figure 328: Example of HTML Source view in Writer/Web
Writer/Web can also display the source code of an HTML document. Go to View > HTML Source
on the Menu bar to open the source code display for an HTML document (Figure 328). The
HTML Source display mode is used to change the formatting and page elements of a web page.
Using this display mode for editing requires familiarity and knowledge of the HTML markup
language.

Notes
HTML markup language has fewer formatting options than a ODF text document.
Writer/Web does not provide all formatting features for HTML documents and
some formatting dialogs have fewer options available. For example, a HTML
paragraph has no tab settings.
HTML markup content generated by Writer/Web is limited to the elements used to
produce a displayable document in a web browser. It does not contain other
components of a website such as external cascading style sheets (CSS), external
JavaScript, or other script languages. When you manually insert links to any
external components into the web page, you must do it in HTML Source display
mode.

HTML files using Writer/Web | 393

Creating and editing
----------------------------------------------------------------------

To create an HTML document, do the following:
1)

Select File > New > HTML Document and Writer/Web opens a blank document in Web
display mode (Figure 327).

2)

Add content to the document by typing or pasting text, images, tables, and other objects.

3)

Use all the formatting resources available in Writer/Web, including the capability to edit
and format the content in styles.

4)

When all editing is complete, go to File > Save As on the Menu bar and save the
document in the HTML file type.

5)

Preview the HTML document in a browser to make sure it has rendered correctly.

Editing source code
----------------------------------------------------------------------

To edit the source code of an HTML document:
1)

Open or create an HTML document.

2)

Open HTML source view (Figure 328) using one of the following methods:
– Go to View > HTML Source on the Menu bar.
– Click on HTML source on the Standard toolbar.

3)

Add, or edit the HTML source code.

4)

When all editing is complete, go to File > Save As on the Menu bar and save the
document as HTML file type.

5)

Preview the HTML document in a browser to make sure renders correctly.

Previewing HTML documents
----------------------------------------------------------------------

It is important to preview HTML documents in a web browser to make sure it displays correctly.
Since not all browsers render HTML files the same way, you should preview an HTML document
in several browsers.
To make LibreOffice open the default web browser and display an HTML document, use one of
the following methods:
•

Go to File > Preview in Web Browser on the Menu bar.

•

Click Preview in Web Browser on the Standard toolbar.

•

Open the web browser and then open the HTML file in the browser.

Writer/Web options
----------------------------------------------------------------------

Go to Tools > Options > LibreOffice Writer/Web (macOS LibreOffice > Preferences >
LibreOffice Writer/Web) on the Menu bar to open the Options LibreOffice Writer/Web dialog
(Figure 329), and then you can define the basic settings for LibreOffice documents in HTML
format. For more information on the options available for Writer/Web, go to the LibreOffice Help
website.
Click on a tab in the dialog to access the available options. The tabbed pages are as follows:
View
Defines the default settings for displaying objects in text documents and also the default
settings for the window elements.

394 | Chapter 10 Working with File Formats, Security, and Exporting

Figure 329: Options LibreOffice Writer/Web dialog
Formatting Aids
Defines the LibreOffice text and HTML documents’ display for certain characters and for
the direct cursor.
Grid
Specifies the settings for the configurable grid for document pages. This grid helps to
determine the exact position of objects. Also, this grid can be set to align with the snap
grid in LibreOffice.
Print
Specifies print settings within a text or HTML document.
Table
Defines the attributes of tables in text documents.
Background
Specifies the background for HTML documents. The background is valid for creating new
HTML documents and for HTML documents already created. Any created HTML
documents must not have a background defined to use this option.

Emailing documents
======================================================================

LibreOffice has multiple ways to send documents as email attachments in one of three formats —
Open Document Format (LibreOffice default format); Microsoft Office format; Portable Document
Format.
1)

Go to File > Send on the Menu bar and use one of the following options:
– Email Document — The default email program is opened and the document is
attached to the email message.
– Email as OpenDocument text — The default email program is opened and the
document is attached to the email message.
– Email as Microsoft Word — LibreOffice creates a file in Microsoft Word format,
opens the default email program, and the document is attached to the email
message.
– Email as PDF — First, the PDF Options dialog opens. Next, select the required
settings required and click OK. LibreOffice will open the default email program with
the PDF file attached to the email message.

Emailing documents | 395

2)

Enter the recipient name, subject, and message, then send the email.

Note
The above procedure is for sending text documents as an attachment to an email.
When sending spreadsheets, presentations, or drawings, the email options
change to reflect the type of document being attached to an email message.

Files on remote servers
======================================================================

LibreOffice can open and save files stored on remote servers. Keeping files on remote servers
allows access to documents using different computers. For example, working on a document in
the office during the day and edit the same document at home for last-minute changes. Storing
files on a remote server also backs up documents from computer loss or hard disk failure. Some
remote servers can also check-in and check-out files controlling usage and access for
documents.
LibreOffice supports many document servers that use well known network protocols such as FTP,
WebDav, Windows share, and SSH. It also supports popular services like Google Drive and
Microsoft OneNote, as well as commercial and open source servers that implement the OASIS
CMIS standard.
Access a remote server connection as follows. The following procedure is an example only.
Actual procedure depends on operating system, computer setup and type of remote file service
selected.
1)

Open the Remote Files dialog (Figure 330) using one of the following methods:
– Click on Remote Files in the LibreOffice Start Center.
– Select File > Open Remote on the Menu bar.
– Select File > Save Remote on the Menu bar.

2)

Click on Manage Services, and select Add service to open the File Services dialog
(Figure 331).

Figure 330: Remote Files dialog

396 | Chapter 10 Working with File Formats, Security, and Exporting

Figure 331: File Services dialog
3)

Select the type of file service required from options available in the Type drop-down list.
Depending on the file service selected, different parameters are necessary for connection
to a remote server.

4)

Enter the necessary information in the text boxes. The text boxes change depending on
the type of service that has been selected in Type.

5)

If necessary, enter a label for the remote server in the Label text box.

6)

Click on OK to save the details and close the File Services dialog.

7)

In the Remote Files dialog, select the service from the Service drop-down list.

8)

Navigate to where the remote file is located and select the required file.

9)

Click on Open to open the file and close the Remote Files dialog.

Digital signatures
======================================================================

To sign a file digitally, a personal key, also known as a certificate, is required. This personal key is
stored on the computer being used as a combination of a private key, which must be kept secret,
and a public key. These keys are added to a drawing when a digital signature is applied. A
certificate is obtained from a certification authority, which may be a private company or a
government institution.
When a digital signature is applied to a document, a checksum is computed from the document
content, plus the personal key being used. The checksum and public key are stored together with
the document.
When the document is opened on another computer with a recent version of LibreOffice, the
program computes the checksum again and compares it with the stored checksum. If both
checksums are the same, the program opens the original, unchanged document.
In addition, the program can display the public key information from the certificate. This
information can then be compared with the public key that is published on the web site of the
certificate authority. Whenever a document is changed, this change breaks the digital signature.
For a more information on digital signatures, see “About Digital Signatures” and “Applying Digital
Signatures” on the LibreOffice Help website.

Digital signatures | 397

Figure 332: Digital Signatures dialog

Figure 333: Select Certificate dialog

Applying digital signatures
This is a sample method for digitally signing a document in LibreOffice. Your actual procedure
depends on how your is computer set up and what operating system is being used.
1)

Go to File > Digital Signatures > Digital Signatures on the Menu bar and open the
Digital Signatures dialog (Figure 332) that lists the available digital signatures for the
document.

2)

If a message box opens advising to save the document, click on Yes to save the
document.

3)

If necessary, click on Sign Document to open the Select Certificate dialog (Figure 333).

4)

Select the required digital signature in the Select Certificate dialog.

5)

Click on Sign to apply the digital signature to the document and close the Select
Certificate dialog.

6)

In the Digital Signatures dialog, select the required digital signature from the signature list.

7)

Click on Close to apply the selected digital signature to the document and close the
Digital Signatures dialog.

398 | Chapter 10 Working with File Formats, Security, and Exporting

8)

Go to File > Save on the Menu bar to save the document.

Notes
A signed document displays a Digital Signature icon in the Status Bar.
Double-click on this Digital Signature icon to view the certificate. More than one
digital signature can be added to a document.
Changing an existing description invalidates a digital signature. However, multiple
digital signatures from the same author are allowed, because each digital
signature can have a different description.

Signature line
Graphic boxes, that includes a signature line, can also be added to a document. This allows the
user to optionally sign a document with their signature. This option is only available for Writer and
Calc documents.
Add a graphic signature box to a Writer, or Calc document as follows:
1)

Go to Insert > Signature Line on the Menu bar to open the Signature Line dialog
(Figure 334).

2)

Enter the necessary details and select the required options.

3)

Click OK to close the Signature Line dialog and a graphic box with a signature line is
inserted into the document. An example is shown in Figure 335.

Figure 334: Signature Line dialog

Figure 335: Example of a signature box

Digital signatures | 399

Figure 336: Drawing Object Properties dialog
4)

Click on the signature box to select it and display the object selection handles.

5)

Use the keyboard arrow keys to move the signature box to the required position on the
page. The normal position for a signature box is at the bottom of a page.

6)

Right click on the selected signature box to open the Drawing Object Properties toolbar
(Figure 336).

7)

Click on Select anchor for object and select the required anchor type from the options
available in the drop-down list.

8)

If necessary, use the other tools available on the Drawing Object Properties toolbar to
format the signature box to the document requirements.

9)

Deselect the signature box to close the Drawing Object Properties toolbar.

10)

Save the document fix the signature box into the document.

Document properties
To open a document’s Properties dialog (Figure 337), go to File > Properties on the Menu bar.
The tabbed pages in the Properties dialog provides information about the document and allows
the document’s properties to be changed.

Figure 337: Properties dialog

400 | Chapter 10 Working with File Formats, Security, and Exporting

General
----------------------------------------------------------------------

Contains basic information about the current file as follows:
File
Displays the file name.
Change Password
Opens a dialog to change the password if a password has been set for the file.
Type
Displays the file type for the current document.
Location
Displays the path and the name of the directory where the file is stored.
Size
Displays the size of the current document in bytes.
Created
Displays the date and time and author when the file was first saved
Modified
Displays the date and time and author when the file was last saved in a LibreOffice file
format.
Template
Displays the template that was used to create the file.
Digitally signed
Displays the date and the time when the file was last signed as well as the name of the
author who signed the document.
Digital Signatures
Opens the Digital Signatures dialog box where digital signatures are managed for the
current document.
Last printed
Displays the date, time and user name when the file was last printed.

Note
After printing, a document must be saved to preserve the Last printed data. No
warning message is displayed if an unsaved document is closed.
Total editing time
Displays the amount of time that the file has been open for editing since the file was
created. The editing time is updated when the file is saved.
Revision number
Displays the number of times that the file has been saved.
Apply user data
Saves the full name of the user with the file. The user data can be changed by going to
Tools > Options > LibreOffice > User Data (macOS LibreOffice > Preferences >
LibreOffice > User Data) on the Menu bar.
Reset Properties
Resets the editing time to zero, the creation date to the current date and time, and the
version number to 1. The modification and printing dates are also deleted.

Document properties | 401

Save preview image with this document
Saves a thumbnail preview in PNG format inside the document. This image may be used
by a file manager under certain conditions.
Preferred resolution for images
Select this option and enter a value in Points Per Inch (ppi) for the preferred image
resolution. This is used as default when an image is inserted into a Writer, Impress, or
Draw document and resize images according to the value in the list box.
Reset
Resets any changes made to the document and is available for all tabbed pages in the
Properties dialog.

Description
----------------------------------------------------------------------

Contains optional editable descriptive information about the document, which may be exported
as metadata to other file formats.
Title
Enter a title for the document.
Subject
Enter a subject for the document. A subject can be used to group documents with similar
contents.
Keywords
Enter the words that required to index the content of the document. Keywords must be
separated by commas. A keyword can contain white space characters, or semicolons.
Comments
Enter comments to help identify the document.

Tip
Title, Subject and Keywords are exported to PDF files as PDF Document
Properties. Entered values are exported and appear in the corresponding fields in
the PDF Document Properties Description.

Custom Properties
----------------------------------------------------------------------

Allows custom information fields to be added to a document. In a new document, this page may
be blank. If the new document is based on a template, this page may contain custom properties.
Properties
Enter the Name, Type and Value for each custom property required. The custom
properties are exported as metadata to other file formats.
Add
Click to add a new row to the custom property list.

Security
----------------------------------------------------------------------

Sets the password options for the current document.
Open file read-only
Select to allow this document to be opened in read-only mode only.

402 | Chapter 10 Working with File Formats, Security, and Exporting

Note
This file sharing option protects the document against accidental changes. It is
still possible to edit a copy of the document and save that copy with the same
name as the original.
Record changes
Select to enable recording changes. This is the same as Edit > Track Changes >
Record on the Menu bar.

Tip
To protect the recording state with a password, select Protect and enter a
password. Other users of this document can apply changes, but cannot disable
change recording without knowing the password.
Protect/Unprotect
Protects the change recording state with a password. If change recording is protected for
the current document, the button is named Unprotect. Click Unprotect and type the
correct password to disable the protection.

Font
----------------------------------------------------------------------

When Embed fonts in the document is selected, any fonts used in the document will be
embedded into the document when it is saved. This may be useful if you are creating a PDF and
want to control how it will look on other computer systems.
Only embed the fonts that are used in your documents. If fonts have been defined for the
document (for example, in the template), but have not been used, select this option to not embed
them. You can choose which types of fonts are embedded: Latin, Asian, Complex.
Font Embedding
Select this option to embed document fonts into the document file and allow portability
between different computer systems. The document with embedded fonts has a larger
size and the fonts are used on the target computer for better rendering of the document
layout.
Consider embedding fonts when a document use rare, or custom fonts not generally
available in other computers.

Note
Font licenses may restrict embedding fonts in documents. Font files contain flags
that indicate if and how they can be embedded within a document file. LibreOffice
parses these flags and determines if and how it may be embedded in a document
file. When opening a document containing embedded fonts, LibreOffice looks at
these flags to determine if and how a document can be viewed or edited.
Font scripts to embed
Select which types of fonts are embedded: Latin, Asian, Complex.

Statistics
----------------------------------------------------------------------

Displays statistics for the current file, for example number of pages, words, and characters.

Document properties | 403

Document classification
======================================================================

Document classification and security is an important issue for businesses and governments.
LibreOffice has implemented the open standards produced by TSCP (Transglobal Secure
Collaboration Participation, Inc.) containing three BAF (Business Authentication Framework)
categories: Intellectual Property, National Security and Export Control with each category having
four BAILS (Business Authorization Identification and Labeling Scheme) levels: Non-Business,
General Business, Confidential, and Internal Only.
While this standard has been developed with the intent that it would be applicable in any domain
of activity, LibreOffice retained the aerospace and defense industry nomenclature and categories,
where sensitivity marking results from national security, export control and intellectual property
policies.
To enable document classification, go to View > Toolbars > TSCP Classification on the Menu
bar to open the TSCP toolbar. This toolbar contains list boxes helping in selection of security for a
document. LibreOffice then adds custom fields in the document properties (File > Properties,
Custom Properties on the Menu bar) to store the classification policy as document metadata.
To prevent a breach in security policy, contents with a higher classification level cannot be pasted
into documents with a lower classification level.

Business Authentication Framework (BAF) Categories
----------------------------------------------------------------------

The default BAF categories for LibreOffice are listed below.
Intellectual Property
Select this category for general purpose document classification.

Tip
The Intellectual Properties category modifies the layout of a document with a
watermark, fields in the header and footer and an information bar on top of the
document area. Each item inserted in the document is controlled by the
classification configuration file.
National Security
Selecting this category assigns the national security policy type to the document. The
selected category is saved together with the document as BAILS metadata in the file
properties and no modifications are carried in the document layout or the user interface.
Export Control
Selects this category assigns the export control policy type to the document. The selected
category is saved together with the document as BAILS metadata in the file properties
and no modifications are carried in the document layout or the user interface.

Note
Refer to the corporate data security policy and information security officers for
support in document classification.

Default levels of classification
----------------------------------------------------------------------

LibreOffice provides default levels of document classification (BAILS) shown below, sorted by
increasing level of business sensitivity:
Non-Business
Information in document has no impact in business, if made public.
404 | Chapter 10 Working with File Formats, Security, and Exporting

General Business
Minor impact. Information has impact in business, can generate embarrassments, minor
damage in brand image, if made public.
Confidential
Modest impact. Information disclosed can damage business brand, can generate
negative media coverage and loss of revenue.
Internal use only
Major damage. Negative national media, lawsuits, fines, long term brand damages.

Customizing classification levels
----------------------------------------------------------------------

LibreOffice allows users to customize the levels of classification for a business. To customize the
number and the name of the levels, copy a file, for example newplan.odt, located in Tools >
Options > LibreOffice > Paths > Classification (macOS LibreOffice > Preferences >
LibreOffice > Paths > Classification) into a local folder and edit the contents. Save the file and
make the required changes to the classification path to access the file.

Pasting contents
----------------------------------------------------------------------

Pasting contents in documents with different levels of classification prevents a breach in the
security policy, contents with high classification level pasted to documents with lower
classification level are not allowed. LibreOffice displays a warning message wherever it detects
that the contents of the clipboard have higher security classification than the target document.

User and personal data
======================================================================

Removing data
----------------------------------------------------------------------

If you need to remove personal data, versions, notes, hidden information, or recorded changes
are removed from a file before sending it to other users, take the following steps:
1)

Go to Tools > Options > LibreOffice > Security (macOS LibreOffice > Preferences >
LibreOffice > Security) on the Menu bar to open the Security page of the Options
LibreOffice dialog.

2)

Click Options to open the Security Options and Warnings dialog (Figure 338).

3)

Select the required options to display warnings and/or set security options. See “Security
options and warnings” on page 457 for more information.

4)

Click OK to close the Security Options and Warnings dialog.

5)

Go to File > Properties on the Menu bar to open the Properties dialog (Figure 337 on
page 451) and click on General to open the General page.

User and personal data | 405

Figure 338: Security Options and Warnings dialog
6)

Deselect the option Apply user data and click on Reset Properties to do the following:
– Removes names in the created and modified fields.
– Deletes modification and printing dates.
– Resets editing time to zero, creation date to the current date and time, and version
number to 1.

7)

Click OK to close the Properties dialog.

8)

Go to File > Versions on the Menu bar, select the versions from the Existing Versions
list and click Delete. Alternatively, go to File > Save As on the Menu bar and save the file
with a different name.

Security options and warnings
----------------------------------------------------------------------

The Security Options and Warnings dialog allows users to set the following options:
When saving or sending
Select to see a warning dialog when saving or sending a document that contains
recorded changes, versions, or comments
When printing
Select to see a warning dialog when printing a document that contains recorded changes
or comments.
When signing
Select to see a warning dialog when signing a document that contains recorded changes,
versions, fields, references to other sources (for example linked sections or linked
pictures), or comments.
When creating PDF files
Select to see a warning dialog when you exporting a document to PDF format that
displays recorded changes in Writer, or displays comments.
Remove personal information on saving
Select to always remove user data from file properties, comments and tracked changes.
The names of authors in comments and changes are replaced by generic values as
"Author1", "Author2" and so forth. Time values are reset to a single standard value. If this
option is not selected, personal information can still be removed for the current document
using Reset Properties on the General page of the Properties dialog.

406 | Chapter 10 Working with File Formats, Security, and Exporting

Recommend password protection on saving
Select to always enable the Save with password option in the file save dialogs. Deselect
the option to save files by default without password.
Ctrl-click required to follow hyperlinks
If enabled, hold down the Ctrl key (macOS ⌘) while clicking a hyperlink to open the
link. If not enabled, a click opens the hyperlink.
Block any links from documents not among the trusted locations (see Macro Security)
Blocks the use of linked images by documents not in the trusted locations defined in
Trusted Sources of the Macro Security dialog. This can increase security if working with
documents from untrusted sources (for example the internet) and are worried about
vulnerabilities in image processing software components. Blocking the use of links means
that images are not loaded in untrusted documents, only a placeholder frame is visible.

Redaction
======================================================================

LibreOffice documents can be redacted to remove, or hide, any sensitive information allowing
selective disclosure of information in a document while keeping other parts of the document
secret. When a LibreOffice document is redacted, it is exported as a new PDF file with all the
redacted portions removed and replaced by redaction blocks of pixels preventing any attempt to
restore or copy the original contents. A redacted document is exported in PDF format for
publication, or sharing.
A copy of any documents redacted in LibreOffice Writer, Calc, or Impress are automatically
transferred to LibreOffice Draw where the redaction is carried out.

Redaction tools
----------------------------------------------------------------------

The tools available on the Redaction toolbar (Figure 339) are as follows:
Rectangle Redaction
Used to mark the content for redaction by drawing transparent rectangles covering the
content. Use the handles to resize the redaction rectangle.
Freeform Redaction
Allows the user to mark the content for redaction by drawing free-form lines, or polygons
covering the content.
Redacted Export (lack)
Converts the semi-transparent redaction shape to opaque black and exports as pixels in
the PDF file.
Redacted Export (White)
Converts the semi-transparent redaction shapes to opaque white shapes and exports as
pixels in the PDF file.
Export Preview PDF
Makes a copy of the presentation as a PDF file to preview the redaction areas before
making a redacted PDF file of the presentation.

Figure 339: Redaction toolbar

Redaction | 407

Documents, spreadsheets, or presentations
----------------------------------------------------------------------

A copy of a document, spreadsheet, or presentation is automatically transferred to LibreOffice
Draw where the redaction is carried out.
1)

Open the document to be redacted in LibreOffice Writer, Calc or Impress, then go to
Tools > Redact on the Menu bar and the following happens:
– The document is copied, prepared and transferred to LibreOffice Draw as an untitled
file.
– LibreOffice Draw opens with the untitled document displayed.
– The Redaction toolbar automatically opens. If the Redaction toolbar is not displayed,
go to View > Toolbars on the Menu bar in LibreOffice Draw and select Redaction.

2)

Go to Tools > Redact on the Menu bar and click on Rectangle Redaction or Freeform
Redaction in the Redaction toolbar.

3)

Draw the required shapes to redact the sensitive areas in the document. The redaction
shape is gray allowing the sensitive areas in the document to be visible before they are
redacted.

4)

If necessary, click on Export Preview PDF to create a preview copy of the PDF file to
review the redaction areas before the redaction is finalized.

5)

If necessary, delete the PDF copy after reviewing the redaction areas in the file.

6)

Click on Redacted Export (White), or Redacted Export (Black) in the Redaction toolbar
to export the presentation file as a redacted PDF file.

7)

Navigate to the folder in the file browser window that opens where the redact PDF file is
going to be saved and enter a name for the file.

8)

Click on Save to create the redacted PDF file. The gray redaction shapes are converted
to white, or black shapes and the document is exported as a PDF

Drawings
----------------------------------------------------------------------

Open a drawing file in Draw, then use Steps 2) thru 8) in “Documents, spreadsheets, or
presentations” on page 459 to create a redacted PDF copy of the drawing file.

Note
When a redacted document is exported as a new PDF file, any redacted areas
are removed from the new document and replaced by redacted blocks of pixels.
These blocks of pixels prevent any attempt to restore, or copying the original
contents that have been redacted.

Automatic redaction
----------------------------------------------------------------------

When LibreOffice conducts automatic redaction, it allows the user to define words and patterns
that are automatically marked for redaction. Automatic redaction is useful for documents that
have multiple occurrences of names and other personal information (for example credit cards,
phone numbers, and so on). Manually redacting this type information in a document would
require significant effort, but automatic redaction makes redaction of a document easier and
more efficient.

408 | Chapter 10 Working with File Formats, Security, and Exporting

Figure 340: Automatic Redaction dialog

Figure 341: Add Target dialog

Creating targets
Targets are rules and patterns used by automatic redaction to find words and information in a
document that are to be marked for automatic redaction.
1)

Open a document and use Tools > Auto-Redact on the Menu bar to open the Automatic
Redaction dialog (Figure 340).

2)

Click on Add Target to open the Add Target dialog (Figure 341).

3)

Enter a target name in the Name text box.

4)

Select a target type from the available options in the Type drop-down list.
– Text — automatic redaction looks for all occurrences of the specified text and marks
them for redaction.
– Regular expression — define a regular expression for searching in a document. All
matches are marked for redaction.
– Predefined — select predefined regular expressions for automatic redaction, such as
credit card numbers, email addresses and so on.

5)

Enter the content in the Content text box.

6)

If necessary, select the options Match case and Whole words only to help define which
targets are auto-redacted.

Redaction | 409

7)

Click OK to close the Add Target dialog and the target is added to the Redaction Targets
list in the Automatic Redaction dialog.

8)

Repeat Steps 2 thru 7 above until all targets required have been added to the document.

9)

Click OK to close the Automatic Redaction dialog. This opens the document as a drawing
in LibreOffice Draw with all targets automatically redacted using Rectangle Redaction.

10)

Print the document, or export the document as a PDF file.

Exporting targets
1)

Open a document where targets for automatic redaction have been added.

2)

Go to Tools > Auto-Redact on the Menu bar to open the Automatic Redaction dialog.

3)

Select the targets for export in the Redaction Targets list.

4)

Click on Save Targets to open the Save Targets dialog and navigate to the location
where the JSON file is going to be saved.

5)

Enter a file name for the JSON file in the File name text box.

6)

Click on Save to save the JSON file and close the Save Targets dialog.

7)

Click OK to close the Automatic Redaction dialog.

Importing targets
1)

Open a document where targets for automatic redaction are going to be used.

2)

Go to Tools > Auto-Redact on the Menu bar to open the Automatic Redaction dialog.

3)

Click on Load Targets to open the Load Targets dialog and navigate to the location of the
JSON file.

4)

Select the required file and click on Open to import the targets into the document and
close the Load Targets dialog.

5)

Click OK to close the Automatic Redaction dialog. This opens the document as a drawing
in LibreOffice Draw with all targets automatically redacted using Rectangle Redaction.

6)

Print the document, or export the document as a PDF file.

Note
The automatic redaction targets are saved in a document. The targets are
available after the document is saved and closed.

Password protection and OpenPGP encryption
======================================================================

LibreOffice provides two types of document protection: password protection and OpenPGP
encryption.
•

Files encrypted with the Save password option enabled cannot be decrypted without
the password.

•

Files encrypted with OpenPGP encryption, the document is encrypted using an algorithm,
which requires a key. Each key is used only once and is sent to the recipient along with
the document.

410 | Chapter 10 Working with File Formats, Security, and Exporting

Figure 342: Save as dialog

Figure 343: Set Password dialog

Password protection
----------------------------------------------------------------------

LibreOffice provides two levels of password protection:
Password protection and OpenPGP encryption | 411

•

The document file cannot be opened without entering a password.

•

The document cannot be edited until a second password is entered.

The two options above make a document available for reading by one group of people and for
reading and editing by a different group. This is compatible with Microsoft Word file protection.

Adding passwords
1)

Go to File > Save As on the Menu bar to open the Save as dialog (Figure 342).

2)

Navigate to the folder where the file is going to be saved.

3)

If necessary, enter a file name in the File name text box and select the file type from the
available options in the File type drop-down list.

4)

Select the Save with password option, then click on Save to open the Set Password
dialog (Figure 343).

5)

In File Encryption Password, enter a password to open the document and then enter
the same password as confirmation. Passwords are case sensitive.

6)

Click on Options to open File Sharing Password.

7)

Select Open file read-only to prevent any editing being carried out on the document.

8)

To allow editing of the document, enter a password in Enter password to allow editing
and repeat the password as confirmation.

9)

Click OK and the Set Password dialog closes and the file is saved with password
protection.

Notes
If the passwords match, the document is saved password protected. If either the
passwords do not match, an error message is displayed.
LibreOffice uses a very strong encryption mechanism that makes it almost
impossible to recover the contents of a document if the password is lost or
forgotten.

Changing passwords
When a document is password protected, the password can be changed while the document is
open.
1)

Go to File > Properties > General on the Menu bar to open the Properties dialog.

2)

Click on Change Password to open the Set Password dialog.

3)

Enter a new password to open the file and to allow editing of the document.

4)

Click OK to close the Set Password dialog.

5)

Click OK again to close the Properties dialog.

OpenPGP encryption
----------------------------------------------------------------------

LibreOffice can encrypt documents confidentially using OpenPGP. The document is encrypted
using a symmetric encryption algorithm, which requires a symmetric key. Each symmetric key is
used only once and is also called a session key. The document and its session key are sent to
the recipient. The session key must be sent to the recipients so they know how to decrypt the
document. To protect the document during transmission, it is encrypted with the public key
belonging to the recipient. Only the private key belonging to the recipient can decrypt the session
key. For more information on using OpenPGP encryption, go to the LibreOffice Help website.
412 | Chapter 10 Working with File Formats, Security, and Exporting

LibreOffice uses the OpenPGP software installed on a computer. If no OpenPGP software is
available, download and install OpenPGP software that is compatible with the computer
operating system before using OpenPGP encryption.
A personal pair of cryptography keys must be defined using the OpenPGP software. Refer to the
OpenPGP software installed on how to create a pair of keys.
OpenPGP encryption requires the use of the public key belonging to the recipient. This key must
be available in the OpenPGP key chain stored in the computer.
The following is an example of how to use OpenPGP encryption on a document:
1)

Set the preferred public key for OpenPGP encryption and digital signature. This preferred
key is pre-selected in key selection dialog each time a document is signed or encrypted.
This removes the requirement to select the preferred key when frequently signing a
document with one specific key.

2)

Go to Tools > Options > LibreOffice > User Data (macOS LibreOffice > Preferences >
LibreOffice > User Data) on the Menu bar and select the following options in the
Cryptography section:
– OpenPGP signing key — select an OpenPGP key from the drop-down list for signing
ODF documents.
– OpenPGP encryption key — select an OpenPGP key from the drop-down list for
encrypting ODF documents.
– When encrypting documents, always encrypt to self — select this option to also
encrypt the file with a public key, allowing the document to be opened with a private
key.

Note
Keep this option selected to allow decryption of documents that have been
encrypted for other people.
3)

Go to File > Save As on the Menu bar to open the Save as dialog.

4)

Navigate to the required location for the file, then enter a file name and file type in the
Save as dialog.

5)

Select Encrypt with GPG key option and click on Save to open the Select X.509
Certificate dialog.

6)

Select the public key for the recipient. Multiple keys can be selected.

7)

Click Encrypt to close the dialog and save the file encrypted with the selected public
keys.

Password protection and OpenPGP encryption | 413

Getting Started Guide 7.6

----

.. rubric:: 章末注
