



<!DOCTYPE html>
<html>
<head>
 <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
 <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" >
 
 <meta name="ROBOTS" content="NOARCHIVE">
 
 <link rel="icon" type="image/vnd.microsoft.icon" href="https://ssl.gstatic.com/codesite/ph/images/phosting.ico">
 
 
 <script type="text/javascript">
 
 
 
 
 var codesite_token = null;
 
 
 var CS_env = {"relativeBaseUrl": "", "projectName": "pybgpdump", "assetHostPath": "https://ssl.gstatic.com/codesite/ph", "assetVersionPath": "https://ssl.gstatic.com/codesite/ph/3076573747170053082", "domainName": null, "profileUrl": null, "projectHomeUrl": "/p/pybgpdump", "loggedInUserEmail": null, "token": null};
 var _gaq = _gaq || [];
 _gaq.push(
 ['siteTracker._setAccount', 'UA-18071-1'],
 ['siteTracker._trackPageview']);
 
 _gaq.push(
 ['projectTracker._setAccount', 'UA-550021-3'],
 ['projectTracker._trackPageview']);
 
 (function() {
 var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
 ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
 (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(ga);
 })();
 
 </script>
 
 
 <title>aspath.py - 
 pybgpdump -
 
 
 MRT and BGP parsing in python - Google Project Hosting
 </title>
 <link type="text/css" rel="stylesheet" href="https://ssl.gstatic.com/codesite/ph/3076573747170053082/css/core.css">
 
 <link type="text/css" rel="stylesheet" href="https://ssl.gstatic.com/codesite/ph/3076573747170053082/css/ph_detail.css" >
 
 
 <link type="text/css" rel="stylesheet" href="https://ssl.gstatic.com/codesite/ph/3076573747170053082/css/d_sb.css" >
 
 
 
<!--[if IE]>
 <link type="text/css" rel="stylesheet" href="https://ssl.gstatic.com/codesite/ph/3076573747170053082/css/d_ie.css" >
<![endif]-->
 <style type="text/css">
 .menuIcon.off { background: no-repeat url(https://ssl.gstatic.com/codesite/ph/images/dropdown_sprite.gif) 0 -42px }
 .menuIcon.on { background: no-repeat url(https://ssl.gstatic.com/codesite/ph/images/dropdown_sprite.gif) 0 -28px }
 .menuIcon.down { background: no-repeat url(https://ssl.gstatic.com/codesite/ph/images/dropdown_sprite.gif) 0 0; }
 
 
 
  tr.inline_comment {
 background: #fff;
 vertical-align: top;
 }
 div.draft, div.published {
 padding: .3em;
 border: 1px solid #999; 
 margin-bottom: .1em;
 font-family: arial, sans-serif;
 max-width: 60em;
 }
 div.draft {
 background: #ffa;
 } 
 div.published {
 background: #e5ecf9;
 }
 div.published .body, div.draft .body {
 padding: .5em .1em .1em .1em;
 max-width: 60em;
 white-space: pre-wrap;
 white-space: -moz-pre-wrap;
 white-space: -pre-wrap;
 white-space: -o-pre-wrap;
 word-wrap: break-word;
 font-size: 1em;
 }
 div.draft .actions {
 margin-left: 1em;
 font-size: 90%;
 }
 div.draft form {
 padding: .5em .5em .5em 0;
 }
 div.draft textarea, div.published textarea {
 width: 95%;
 height: 10em;
 font-family: arial, sans-serif;
 margin-bottom: .5em;
 }

 
 .nocursor, .nocursor td, .cursor_hidden, .cursor_hidden td {
 background-color: white;
 height: 2px;
 }
 .cursor, .cursor td {
 background-color: darkblue;
 height: 2px;
 display: '';
 }
 
 
.list {
 border: 1px solid white;
 border-bottom: 0;
}

 
 </style>
</head>
<body class="t4">
<script type="text/javascript">
 window.___gcfg = {lang: 'en'};
 (function() 
 {var po = document.createElement("script");
 po.type = "text/javascript"; po.async = true;po.src = "https://apis.google.com/js/plusone.js";
 var s = document.getElementsByTagName("script")[0];
 s.parentNode.insertBefore(po, s);
 })();
</script>
<div class="headbg">

 <div id="gaia">
 

 <span>
 
 
 <a href="#" id="projects-dropdown" onclick="return false;"><u>My favorites</u> <small>&#9660;</small></a>
 | <a href="https://www.google.com/accounts/ServiceLogin?service=code&amp;ltmpl=phosting&amp;continue=https%3A%2F%2Fcode.google.com%2Fp%2Fpybgpdump%2Fsource%2Fbrowse%2Ftrunk%2Fsamples%2Faspath.py&amp;followup=https%3A%2F%2Fcode.google.com%2Fp%2Fpybgpdump%2Fsource%2Fbrowse%2Ftrunk%2Fsamples%2Faspath.py" onclick="_CS_click('/gb/ph/signin');"><u>Sign in</u></a>
 
 </span>

 </div>

 <div class="gbh" style="left: 0pt;"></div>
 <div class="gbh" style="right: 0pt;"></div>
 
 
 <div style="height: 1px"></div>
<!--[if lte IE 7]>
<div style="text-align:center;">
Your version of Internet Explorer is not supported. Try a browser that
contributes to open source, such as <a href="http://www.firefox.com">Firefox</a>,
<a href="http://www.google.com/chrome">Google Chrome</a>, or
<a href="http://code.google.com/chrome/chromeframe/">Google Chrome Frame</a>.
</div>
<![endif]-->



 <table style="padding:0px; margin: 0px 0px 10px 0px; width:100%" cellpadding="0" cellspacing="0"
 itemscope itemtype="http://schema.org/CreativeWork">
 <tr style="height: 58px;">
 
 
 
 <td id="plogo">
 <link itemprop="url" href="/p/pybgpdump">
 <a href="/p/pybgpdump/">
 
 <img src="https://ssl.gstatic.com/codesite/ph/images/defaultlogo.png" alt="Logo" itemprop="image">
 
 </a>
 </td>
 
 <td style="padding-left: 0.5em">
 
 <div id="pname">
 <a href="/p/pybgpdump/"><span itemprop="name">pybgpdump</span></a>
 </div>
 
 <div id="psum">
 <a id="project_summary_link"
 href="/p/pybgpdump/"><span itemprop="description">MRT and BGP parsing in python</span></a>
 
 </div>
 
 
 </td>
 <td style="white-space:nowrap;text-align:right; vertical-align:bottom;">
 
 <form action="/hosting/search">
 <input size="30" name="q" value="" type="text">
 
 <input type="submit" name="projectsearch" value="Search projects" >
 </form>
 
 </tr>
 </table>

</div>

 
<div id="mt" class="gtb"> 
 <a href="/p/pybgpdump/" class="tab ">Project&nbsp;Home</a>
 
 
 
 
 <a href="/p/pybgpdump/downloads/list" class="tab ">Downloads</a>
 
 
 
 
 
 <a href="/p/pybgpdump/w/list" class="tab ">Wiki</a>
 
 
 
 
 
 <a href="/p/pybgpdump/issues/list"
 class="tab ">Issues</a>
 
 
 
 
 
 <a href="/p/pybgpdump/source/checkout"
 class="tab active">Source</a>
 
 
 
 
 
 
 
 
 <div class=gtbc></div>
</div>
<table cellspacing="0" cellpadding="0" width="100%" align="center" border="0" class="st">
 <tr>
 
 
 
 
 
 
 <td class="subt">
 <div class="st2">
 <div class="isf">
 
 


 <span class="inst1"><a href="/p/pybgpdump/source/checkout">Checkout</a></span> &nbsp;
 <span class="inst2"><a href="/p/pybgpdump/source/browse/">Browse</a></span> &nbsp;
 <span class="inst3"><a href="/p/pybgpdump/source/list">Changes</a></span> &nbsp;
 
 
 
 
 
 
 
 </form>
 <script type="text/javascript">
 
 function codesearchQuery(form) {
 var query = document.getElementById('q').value;
 if (query) { form.action += '%20' + query; }
 }
 </script>
 </div>
</div>

 </td>
 
 
 
 <td align="right" valign="top" class="bevel-right"></td>
 </tr>
</table>


<script type="text/javascript">
 var cancelBubble = false;
 function _go(url) { document.location = url; }
</script>
<div id="maincol"
 
>

 




<div class="expand">
<div id="colcontrol">
<style type="text/css">
 #file_flipper { white-space: nowrap; padding-right: 2em; }
 #file_flipper.hidden { display: none; }
 #file_flipper .pagelink { color: #0000CC; text-decoration: underline; }
 #file_flipper #visiblefiles { padding-left: 0.5em; padding-right: 0.5em; }
</style>
<table id="nav_and_rev" class="list"
 cellpadding="0" cellspacing="0" width="100%">
 <tr>
 
 <td nowrap="nowrap" class="src_crumbs src_nav" width="33%">
 <strong class="src_nav">Source path:&nbsp;</strong>
 <span id="crumb_root">
 
 <a href="/p/pybgpdump/source/browse/">svn</a>/&nbsp;</span>
 <span id="crumb_links" class="ifClosed"><a href="/p/pybgpdump/source/browse/trunk/">trunk</a><span class="sp">/&nbsp;</span><a href="/p/pybgpdump/source/browse/trunk/samples/">samples</a><span class="sp">/&nbsp;</span>aspath.py</span>
 
 


 </td>
 
 
 <td nowrap="nowrap" width="33%" align="right">
 <table cellpadding="0" cellspacing="0" style="font-size: 100%"><tr>
 
 
 <td class="flipper"><b>r10</b></td>
 
 </tr></table>
 </td> 
 </tr>
</table>

<div class="fc">
 
 
 
<style type="text/css">
.undermouse span {
 background-image: url(https://ssl.gstatic.com/codesite/ph/images/comments.gif); }
</style>
<table class="opened" id="review_comment_area"
><tr>
<td id="nums">
<pre><table width="100%"><tr class="nocursor"><td></td></tr></table></pre>
<pre><table width="100%" id="nums_table_0"><tr id="gr_svn10_1"

><td id="1"><a href="#1">1</a></td></tr
><tr id="gr_svn10_2"

><td id="2"><a href="#2">2</a></td></tr
><tr id="gr_svn10_3"

><td id="3"><a href="#3">3</a></td></tr
><tr id="gr_svn10_4"

><td id="4"><a href="#4">4</a></td></tr
><tr id="gr_svn10_5"

><td id="5"><a href="#5">5</a></td></tr
><tr id="gr_svn10_6"

><td id="6"><a href="#6">6</a></td></tr
><tr id="gr_svn10_7"

><td id="7"><a href="#7">7</a></td></tr
><tr id="gr_svn10_8"

><td id="8"><a href="#8">8</a></td></tr
><tr id="gr_svn10_9"

><td id="9"><a href="#9">9</a></td></tr
><tr id="gr_svn10_10"

><td id="10"><a href="#10">10</a></td></tr
><tr id="gr_svn10_11"

><td id="11"><a href="#11">11</a></td></tr
><tr id="gr_svn10_12"

><td id="12"><a href="#12">12</a></td></tr
><tr id="gr_svn10_13"

><td id="13"><a href="#13">13</a></td></tr
><tr id="gr_svn10_14"

><td id="14"><a href="#14">14</a></td></tr
><tr id="gr_svn10_15"

><td id="15"><a href="#15">15</a></td></tr
><tr id="gr_svn10_16"

><td id="16"><a href="#16">16</a></td></tr
><tr id="gr_svn10_17"

><td id="17"><a href="#17">17</a></td></tr
><tr id="gr_svn10_18"

><td id="18"><a href="#18">18</a></td></tr
><tr id="gr_svn10_19"

><td id="19"><a href="#19">19</a></td></tr
><tr id="gr_svn10_20"

><td id="20"><a href="#20">20</a></td></tr
><tr id="gr_svn10_21"

><td id="21"><a href="#21">21</a></td></tr
><tr id="gr_svn10_22"

><td id="22"><a href="#22">22</a></td></tr
><tr id="gr_svn10_23"

><td id="23"><a href="#23">23</a></td></tr
><tr id="gr_svn10_24"

><td id="24"><a href="#24">24</a></td></tr
><tr id="gr_svn10_25"

><td id="25"><a href="#25">25</a></td></tr
><tr id="gr_svn10_26"

><td id="26"><a href="#26">26</a></td></tr
><tr id="gr_svn10_27"

><td id="27"><a href="#27">27</a></td></tr
><tr id="gr_svn10_28"

><td id="28"><a href="#28">28</a></td></tr
><tr id="gr_svn10_29"

><td id="29"><a href="#29">29</a></td></tr
><tr id="gr_svn10_30"

><td id="30"><a href="#30">30</a></td></tr
><tr id="gr_svn10_31"

><td id="31"><a href="#31">31</a></td></tr
><tr id="gr_svn10_32"

><td id="32"><a href="#32">32</a></td></tr
><tr id="gr_svn10_33"

><td id="33"><a href="#33">33</a></td></tr
><tr id="gr_svn10_34"

><td id="34"><a href="#34">34</a></td></tr
><tr id="gr_svn10_35"

><td id="35"><a href="#35">35</a></td></tr
><tr id="gr_svn10_36"

><td id="36"><a href="#36">36</a></td></tr
><tr id="gr_svn10_37"

><td id="37"><a href="#37">37</a></td></tr
><tr id="gr_svn10_38"

><td id="38"><a href="#38">38</a></td></tr
></table></pre>
<pre><table width="100%"><tr class="nocursor"><td></td></tr></table></pre>
</td>
<td id="lines">
<pre><table width="100%"><tr class="cursor_stop cursor_hidden"><td></td></tr></table></pre>
<pre class="prettyprint lang-py"><table id="src_table_0"><tr
id=sl_svn10_1

><td class="source">#!/usr/bin/env python<br></td></tr
><tr
id=sl_svn10_2

><td class="source"><br></td></tr
><tr
id=sl_svn10_3

><td class="source">from optparse import OptionParser<br></td></tr
><tr
id=sl_svn10_4

><td class="source">from dpkt import bgp<br></td></tr
><tr
id=sl_svn10_5

><td class="source">from pybgpdump import BGPDump<br></td></tr
><tr
id=sl_svn10_6

><td class="source"><br></td></tr
><tr
id=sl_svn10_7

><td class="source">DELIMS = ( (&#39;&#39;, &#39;&#39;),<br></td></tr
><tr
id=sl_svn10_8

><td class="source">           (&#39;{&#39;, &#39;}&#39;),  # AS_SET<br></td></tr
><tr
id=sl_svn10_9

><td class="source">           (&#39;&#39;, &#39;&#39;),    # AS_SEQUENCE<br></td></tr
><tr
id=sl_svn10_10

><td class="source">           (&#39;(&#39;, &#39;)&#39;),  # AS_CONFED_SEQUENCE<br></td></tr
><tr
id=sl_svn10_11

><td class="source">           (&#39;[&#39;, &#39;]&#39;) ) # AS_CONFED_SET<br></td></tr
><tr
id=sl_svn10_12

><td class="source"><br></td></tr
><tr
id=sl_svn10_13

><td class="source">def path_to_str(path):<br></td></tr
><tr
id=sl_svn10_14

><td class="source">    str = &#39;&#39;<br></td></tr
><tr
id=sl_svn10_15

><td class="source">    for seg in path.segments:<br></td></tr
><tr
id=sl_svn10_16

><td class="source">        str += DELIMS[seg.type][0]<br></td></tr
><tr
id=sl_svn10_17

><td class="source">        for AS in seg.path:<br></td></tr
><tr
id=sl_svn10_18

><td class="source">            str += &#39;%d &#39; % (AS)<br></td></tr
><tr
id=sl_svn10_19

><td class="source">        str = str[:-1]<br></td></tr
><tr
id=sl_svn10_20

><td class="source">        str += DELIMS[seg.type][1] + &#39; &#39;<br></td></tr
><tr
id=sl_svn10_21

><td class="source">    return str<br></td></tr
><tr
id=sl_svn10_22

><td class="source"><br></td></tr
><tr
id=sl_svn10_23

><td class="source">def main():<br></td></tr
><tr
id=sl_svn10_24

><td class="source">    parser = OptionParser()<br></td></tr
><tr
id=sl_svn10_25

><td class="source">    parser.add_option(&#39;-i&#39;, &#39;--input&#39;, dest=&#39;input&#39;, default=&#39;sample.dump.gz&#39;,<br></td></tr
><tr
id=sl_svn10_26

><td class="source">                      help=&#39;read input from FILE&#39;, metavar=&#39;FILE&#39;)<br></td></tr
><tr
id=sl_svn10_27

><td class="source">    (options, args) = parser.parse_args()<br></td></tr
><tr
id=sl_svn10_28

><td class="source"><br></td></tr
><tr
id=sl_svn10_29

><td class="source">    dump = BGPDump(options.input)<br></td></tr
><tr
id=sl_svn10_30

><td class="source">    for mrt_h, bgp_h, bgp_m in dump:<br></td></tr
><tr
id=sl_svn10_31

><td class="source">        path = &#39;&#39;<br></td></tr
><tr
id=sl_svn10_32

><td class="source">        for attr in bgp_m.update.attributes:<br></td></tr
><tr
id=sl_svn10_33

><td class="source">            if attr.type == bgp.AS_PATH:<br></td></tr
><tr
id=sl_svn10_34

><td class="source">                print path_to_str(attr.as_path)<br></td></tr
><tr
id=sl_svn10_35

><td class="source">                break<br></td></tr
><tr
id=sl_svn10_36

><td class="source"><br></td></tr
><tr
id=sl_svn10_37

><td class="source">if __name__ == &#39;__main__&#39;:<br></td></tr
><tr
id=sl_svn10_38

><td class="source">    main()<br></td></tr
></table></pre>
<pre><table width="100%"><tr class="cursor_stop cursor_hidden"><td></td></tr></table></pre>
</td>
</tr></table>

 
<script type="text/javascript">
 var lineNumUnderMouse = -1;
 
 function gutterOver(num) {
 gutterOut();
 var newTR = document.getElementById('gr_svn10_' + num);
 if (newTR) {
 newTR.className = 'undermouse';
 }
 lineNumUnderMouse = num;
 }
 function gutterOut() {
 if (lineNumUnderMouse != -1) {
 var oldTR = document.getElementById(
 'gr_svn10_' + lineNumUnderMouse);
 if (oldTR) {
 oldTR.className = '';
 }
 lineNumUnderMouse = -1;
 }
 }
 var numsGenState = {table_base_id: 'nums_table_'};
 var srcGenState = {table_base_id: 'src_table_'};
 var alignerRunning = false;
 var startOver = false;
 function setLineNumberHeights() {
 if (alignerRunning) {
 startOver = true;
 return;
 }
 numsGenState.chunk_id = 0;
 numsGenState.table = document.getElementById('nums_table_0');
 numsGenState.row_num = 0;
 if (!numsGenState.table) {
 return; // Silently exit if no file is present.
 }
 srcGenState.chunk_id = 0;
 srcGenState.table = document.getElementById('src_table_0');
 srcGenState.row_num = 0;
 alignerRunning = true;
 continueToSetLineNumberHeights();
 }
 function rowGenerator(genState) {
 if (genState.row_num < genState.table.rows.length) {
 var currentRow = genState.table.rows[genState.row_num];
 genState.row_num++;
 return currentRow;
 }
 var newTable = document.getElementById(
 genState.table_base_id + (genState.chunk_id + 1));
 if (newTable) {
 genState.chunk_id++;
 genState.row_num = 0;
 genState.table = newTable;
 return genState.table.rows[0];
 }
 return null;
 }
 var MAX_ROWS_PER_PASS = 1000;
 function continueToSetLineNumberHeights() {
 var rowsInThisPass = 0;
 var numRow = 1;
 var srcRow = 1;
 while (numRow && srcRow && rowsInThisPass < MAX_ROWS_PER_PASS) {
 numRow = rowGenerator(numsGenState);
 srcRow = rowGenerator(srcGenState);
 rowsInThisPass++;
 if (numRow && srcRow) {
 if (numRow.offsetHeight != srcRow.offsetHeight) {
 numRow.firstChild.style.height = srcRow.offsetHeight + 'px';
 }
 }
 }
 if (rowsInThisPass >= MAX_ROWS_PER_PASS) {
 setTimeout(continueToSetLineNumberHeights, 10);
 } else {
 alignerRunning = false;
 if (startOver) {
 startOver = false;
 setTimeout(setLineNumberHeights, 500);
 }
 }
 }
 function initLineNumberHeights() {
 // Do 2 complete passes, because there can be races
 // between this code and prettify.
 startOver = true;
 setTimeout(setLineNumberHeights, 250);
 window.onresize = setLineNumberHeights;
 }
 initLineNumberHeights();
</script>

 
 
 <div id="log">
 <div style="text-align:right">
 <a class="ifCollapse" href="#" onclick="_toggleMeta(this); return false">Show details</a>
 <a class="ifExpand" href="#" onclick="_toggleMeta(this); return false">Hide details</a>
 </div>
 <div class="ifExpand">
 
 
 <div class="pmeta_bubble_bg" style="border:1px solid white">
 <div class="round4"></div>
 <div class="round2"></div>
 <div class="round1"></div>
 <div class="box-inner">
 <div id="changelog">
 <p>Change log</p>
 <div>
 <a href="/p/pybgpdump/source/detail?spec=svn10&amp;r=2">r2</a>
 by jon.oberheide
 on Sep 20, 2006
 &nbsp; <a href="/p/pybgpdump/source/diff?spec=svn10&r=2&amp;format=side&amp;path=/trunk/samples/aspath.py&amp;old_path=/trunk/samples/aspath.py&amp;old=">Diff</a>
 </div>
 <pre>initial import (version 0.1)</pre>
 </div>
 
 
 
 
 
 
 <script type="text/javascript">
 var detail_url = '/p/pybgpdump/source/detail?r=2&spec=svn10';
 var publish_url = '/p/pybgpdump/source/detail?r=2&spec=svn10#publish';
 // describe the paths of this revision in javascript.
 var changed_paths = [];
 var changed_urls = [];
 
 changed_paths.push('/trunk/AUTHORS');
 changed_urls.push('/p/pybgpdump/source/browse/trunk/AUTHORS?r\x3d2\x26spec\x3dsvn10');
 
 
 changed_paths.push('/trunk/COPYING');
 changed_urls.push('/p/pybgpdump/source/browse/trunk/COPYING?r\x3d2\x26spec\x3dsvn10');
 
 
 changed_paths.push('/trunk/ChangeLog');
 changed_urls.push('/p/pybgpdump/source/browse/trunk/ChangeLog?r\x3d2\x26spec\x3dsvn10');
 
 
 changed_paths.push('/trunk/Makefile');
 changed_urls.push('/p/pybgpdump/source/browse/trunk/Makefile?r\x3d2\x26spec\x3dsvn10');
 
 
 changed_paths.push('/trunk/README');
 changed_urls.push('/p/pybgpdump/source/browse/trunk/README?r\x3d2\x26spec\x3dsvn10');
 
 
 changed_paths.push('/trunk/TODO');
 changed_urls.push('/p/pybgpdump/source/browse/trunk/TODO?r\x3d2\x26spec\x3dsvn10');
 
 
 changed_paths.push('/trunk/pybgpdump.py');
 changed_urls.push('/p/pybgpdump/source/browse/trunk/pybgpdump.py?r\x3d2\x26spec\x3dsvn10');
 
 
 changed_paths.push('/trunk/samples');
 changed_urls.push('/p/pybgpdump/source/browse/trunk/samples?r\x3d2\x26spec\x3dsvn10');
 
 
 changed_paths.push('/trunk/samples/aspath.py');
 changed_urls.push('/p/pybgpdump/source/browse/trunk/samples/aspath.py?r\x3d2\x26spec\x3dsvn10');
 
 var selected_path = '/trunk/samples/aspath.py';
 
 
 changed_paths.push('/trunk/samples/route_btoa.py');
 changed_urls.push('/p/pybgpdump/source/browse/trunk/samples/route_btoa.py?r\x3d2\x26spec\x3dsvn10');
 
 
 changed_paths.push('/trunk/samples/sample.dump.gz');
 changed_urls.push('/p/pybgpdump/source/browse/trunk/samples/sample.dump.gz?r\x3d2\x26spec\x3dsvn10');
 
 
 changed_paths.push('/trunk/samples/simple.py');
 changed_urls.push('/p/pybgpdump/source/browse/trunk/samples/simple.py?r\x3d2\x26spec\x3dsvn10');
 
 
 changed_paths.push('/trunk/setup.py');
 changed_urls.push('/p/pybgpdump/source/browse/trunk/setup.py?r\x3d2\x26spec\x3dsvn10');
 
 
 function getCurrentPageIndex() {
 for (var i = 0; i < changed_paths.length; i++) {
 if (selected_path == changed_paths[i]) {
 return i;
 }
 }
 }
 function getNextPage() {
 var i = getCurrentPageIndex();
 if (i < changed_paths.length - 1) {
 return changed_urls[i + 1];
 }
 return null;
 }
 function getPreviousPage() {
 var i = getCurrentPageIndex();
 if (i > 0) {
 return changed_urls[i - 1];
 }
 return null;
 }
 function gotoNextPage() {
 var page = getNextPage();
 if (!page) {
 page = detail_url;
 }
 window.location = page;
 }
 function gotoPreviousPage() {
 var page = getPreviousPage();
 if (!page) {
 page = detail_url;
 }
 window.location = page;
 }
 function gotoDetailPage() {
 window.location = detail_url;
 }
 function gotoPublishPage() {
 window.location = publish_url;
 }
</script>

 
 <style type="text/css">
 #review_nav {
 border-top: 3px solid white;
 padding-top: 6px;
 margin-top: 1em;
 }
 #review_nav td {
 vertical-align: middle;
 }
 #review_nav select {
 margin: .5em 0;
 }
 </style>
 <div id="review_nav">
 <table><tr><td>Go to:&nbsp;</td><td>
 <select name="files_in_rev" onchange="window.location=this.value">
 
 <option value="/p/pybgpdump/source/browse/trunk/AUTHORS?r=2&amp;spec=svn10"
 
 >/trunk/AUTHORS</option>
 
 <option value="/p/pybgpdump/source/browse/trunk/COPYING?r=2&amp;spec=svn10"
 
 >/trunk/COPYING</option>
 
 <option value="/p/pybgpdump/source/browse/trunk/ChangeLog?r=2&amp;spec=svn10"
 
 >/trunk/ChangeLog</option>
 
 <option value="/p/pybgpdump/source/browse/trunk/Makefile?r=2&amp;spec=svn10"
 
 >/trunk/Makefile</option>
 
 <option value="/p/pybgpdump/source/browse/trunk/README?r=2&amp;spec=svn10"
 
 >/trunk/README</option>
 
 <option value="/p/pybgpdump/source/browse/trunk/TODO?r=2&amp;spec=svn10"
 
 >/trunk/TODO</option>
 
 <option value="/p/pybgpdump/source/browse/trunk/pybgpdump.py?r=2&amp;spec=svn10"
 
 >/trunk/pybgpdump.py</option>
 
 <option value="/p/pybgpdump/source/browse/trunk/samples?r=2&amp;spec=svn10"
 
 >/trunk/samples</option>
 
 <option value="/p/pybgpdump/source/browse/trunk/samples/aspath.py?r=2&amp;spec=svn10"
 selected="selected"
 >/trunk/samples/aspath.py</option>
 
 <option value="/p/pybgpdump/source/browse/trunk/samples/route_btoa.py?r=2&amp;spec=svn10"
 
 >/trunk/samples/route_btoa.py</option>
 
 <option value="/p/pybgpdump/source/browse/trunk/samples/sample.dump.gz?r=2&amp;spec=svn10"
 
 >/trunk/samples/sample.dump.gz</option>
 
 <option value="/p/pybgpdump/source/browse/trunk/samples/simple.py?r=2&amp;spec=svn10"
 
 >/trunk/samples/simple.py</option>
 
 <option value="/p/pybgpdump/source/browse/trunk/setup.py?r=2&amp;spec=svn10"
 
 >/trunk/setup.py</option>
 
 </select>
 </td></tr></table>
 
 
 



 <div style="white-space:nowrap">
 Project members,
 <a href="https://www.google.com/accounts/ServiceLogin?service=code&amp;ltmpl=phosting&amp;continue=https%3A%2F%2Fcode.google.com%2Fp%2Fpybgpdump%2Fsource%2Fbrowse%2Ftrunk%2Fsamples%2Faspath.py&amp;followup=https%3A%2F%2Fcode.google.com%2Fp%2Fpybgpdump%2Fsource%2Fbrowse%2Ftrunk%2Fsamples%2Faspath.py"
 >sign in</a> to write a code review</div>


 
 </div>
 
 
 </div>
 <div class="round1"></div>
 <div class="round2"></div>
 <div class="round4"></div>
 </div>
 <div class="pmeta_bubble_bg" style="border:1px solid white">
 <div class="round4"></div>
 <div class="round2"></div>
 <div class="round1"></div>
 <div class="box-inner">
 <div id="older_bubble">
 <p>Older revisions</p>
 
 <a href="/p/pybgpdump/source/list?path=/trunk/samples/aspath.py&start=2">All revisions of this file</a>
 </div>
 </div>
 <div class="round1"></div>
 <div class="round2"></div>
 <div class="round4"></div>
 </div>
 
 <div class="pmeta_bubble_bg" style="border:1px solid white">
 <div class="round4"></div>
 <div class="round2"></div>
 <div class="round1"></div>
 <div class="box-inner">
 <div id="fileinfo_bubble">
 <p>File info</p>
 
 <div>Size: 1041 bytes,
 38 lines</div>
 
 <div><a href="//pybgpdump.googlecode.com/svn/trunk/samples/aspath.py">View raw file</a></div>
 </div>
 
 <div id="props">
 <p>File properties</p>
 <dl>
 
 <dt>svn:executable</dt>
 <dd>*</dd>
 
 </dl>
 </div>
 
 </div>
 <div class="round1"></div>
 <div class="round2"></div>
 <div class="round4"></div>
 </div>
 </div>
 </div>


</div>

</div>
</div>

<script src="https://ssl.gstatic.com/codesite/ph/3076573747170053082/js/prettify/prettify.js"></script>
<script type="text/javascript">prettyPrint();</script>


<script src="https://ssl.gstatic.com/codesite/ph/3076573747170053082/js/source_file_scripts.js"></script>

 <script type="text/javascript" src="https://ssl.gstatic.com/codesite/ph/3076573747170053082/js/kibbles.js"></script>
 <script type="text/javascript">
 var lastStop = null;
 var initialized = false;
 
 function updateCursor(next, prev) {
 if (prev && prev.element) {
 prev.element.className = 'cursor_stop cursor_hidden';
 }
 if (next && next.element) {
 next.element.className = 'cursor_stop cursor';
 lastStop = next.index;
 }
 }
 
 function pubRevealed(data) {
 updateCursorForCell(data.cellId, 'cursor_stop cursor_hidden');
 if (initialized) {
 reloadCursors();
 }
 }
 
 function draftRevealed(data) {
 updateCursorForCell(data.cellId, 'cursor_stop cursor_hidden');
 if (initialized) {
 reloadCursors();
 }
 }
 
 function draftDestroyed(data) {
 updateCursorForCell(data.cellId, 'nocursor');
 if (initialized) {
 reloadCursors();
 }
 }
 function reloadCursors() {
 kibbles.skipper.reset();
 loadCursors();
 if (lastStop != null) {
 kibbles.skipper.setCurrentStop(lastStop);
 }
 }
 // possibly the simplest way to insert any newly added comments
 // is to update the class of the corresponding cursor row,
 // then refresh the entire list of rows.
 function updateCursorForCell(cellId, className) {
 var cell = document.getElementById(cellId);
 // we have to go two rows back to find the cursor location
 var row = getPreviousElement(cell.parentNode);
 row.className = className;
 }
 // returns the previous element, ignores text nodes.
 function getPreviousElement(e) {
 var element = e.previousSibling;
 if (element.nodeType == 3) {
 element = element.previousSibling;
 }
 if (element && element.tagName) {
 return element;
 }
 }
 function loadCursors() {
 // register our elements with skipper
 var elements = CR_getElements('*', 'cursor_stop');
 var len = elements.length;
 for (var i = 0; i < len; i++) {
 var element = elements[i]; 
 element.className = 'cursor_stop cursor_hidden';
 kibbles.skipper.append(element);
 }
 }
 function toggleComments() {
 CR_toggleCommentDisplay();
 reloadCursors();
 }
 function keysOnLoadHandler() {
 // setup skipper
 kibbles.skipper.addStopListener(
 kibbles.skipper.LISTENER_TYPE.PRE, updateCursor);
 // Set the 'offset' option to return the middle of the client area
 // an option can be a static value, or a callback
 kibbles.skipper.setOption('padding_top', 50);
 // Set the 'offset' option to return the middle of the client area
 // an option can be a static value, or a callback
 kibbles.skipper.setOption('padding_bottom', 100);
 // Register our keys
 kibbles.skipper.addFwdKey("n");
 kibbles.skipper.addRevKey("p");
 kibbles.keys.addKeyPressListener(
 'u', function() { window.location = detail_url; });
 kibbles.keys.addKeyPressListener(
 'r', function() { window.location = detail_url + '#publish'; });
 
 kibbles.keys.addKeyPressListener('j', gotoNextPage);
 kibbles.keys.addKeyPressListener('k', gotoPreviousPage);
 
 
 }
 </script>
<script src="https://ssl.gstatic.com/codesite/ph/3076573747170053082/js/code_review_scripts.js"></script>
<script type="text/javascript">
 function showPublishInstructions() {
 var element = document.getElementById('review_instr');
 if (element) {
 element.className = 'opened';
 }
 }
 var codereviews;
 function revsOnLoadHandler() {
 // register our source container with the commenting code
 var paths = {'svn10': '/trunk/samples/aspath.py'}
 codereviews = CR_controller.setup(
 {"relativeBaseUrl": "", "projectName": "pybgpdump", "assetHostPath": "https://ssl.gstatic.com/codesite/ph", "assetVersionPath": "https://ssl.gstatic.com/codesite/ph/3076573747170053082", "domainName": null, "profileUrl": null, "projectHomeUrl": "/p/pybgpdump", "loggedInUserEmail": null, "token": null}, '', 'svn10', paths,
 CR_BrowseIntegrationFactory);
 
 codereviews.registerActivityListener(CR_ActivityType.REVEAL_DRAFT_PLATE, showPublishInstructions);
 
 codereviews.registerActivityListener(CR_ActivityType.REVEAL_PUB_PLATE, pubRevealed);
 codereviews.registerActivityListener(CR_ActivityType.REVEAL_DRAFT_PLATE, draftRevealed);
 codereviews.registerActivityListener(CR_ActivityType.DISCARD_DRAFT_COMMENT, draftDestroyed);
 
 
 
 
 
 
 
 var initialized = true;
 reloadCursors();
 }
 window.onload = function() {keysOnLoadHandler(); revsOnLoadHandler();};

</script>
<script type="text/javascript" src="https://ssl.gstatic.com/codesite/ph/3076573747170053082/js/dit_scripts.js"></script>

 
 
 
 <script type="text/javascript" src="https://ssl.gstatic.com/codesite/ph/3076573747170053082/js/ph_core.js"></script>
 
 
 
 
</div> 

<div id="footer" dir="ltr">
 <div class="text">
 <a href="/projecthosting/terms.html">Terms</a> -
 <a href="http://www.google.com/privacy.html">Privacy</a> -
 <a href="/p/support/">Project Hosting Help</a>
 </div>
</div>
 <div class="hostedBy" style="margin-top: -20px;">
 <span style="vertical-align: top;">Powered by <a href="http://code.google.com/projecthosting/">Google Project Hosting</a></span>
 </div>

 
 


 
 </body>
</html>
