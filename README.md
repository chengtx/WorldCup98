# WorldCup98

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
This dataset is used to compared the performance difference between ELK and Splunk.
http://ita.ee.lbl.gov/html/contrib/WorldCup.html

For plain text log, the size of each entry is about 100B (0.1KB).
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


Description
This dataset consists of all the requests made to the 1998 World Cup Web site between April 30, 1998 and July 26, 1998. During this period of time the site received 1,352,804,107 requests.
Format
The access logs from the 1998 World Cup Web site were originally in the Common Log Format. In order to reduce both the size of the logs and the analysis time the access logs were converted to a binary format (big endian = network order). Each entry in the binary log is a fixed size and represents a single request to the site. The format of a request in the binary log looks like:
struct request
{
  uint32_t timestamp;
  uint32_t clientID;
  uint32_t objectID;
  uint32_t size;
  uint8_t method;
  uint8_t status;
  uint8_t type;
  uint8_t server;
};
The fields of the request structure contain the following information:

timestamp - the time of the request, stored as the number of seconds since the Epoch. The timestamp has been converted to GMT to allow for portability. During the World Cup the local time was 2 hours ahead of GMT (+0200). In order to determine the local time, each timestamp must be adjusted by this amount.

clientID - a unique integer identifier for the client that issued the request (this may be a proxy); due to privacy concerns these mappings cannot be released; note that each clientID maps to exactly one IP address, and the mappings are preserved across the entire data set - that is if IP address 0.0.0.0 mapped to clientID X on day Y then any request in any of the data sets containing clientID X also came from IP address 0.0.0.0

objectID - a unique integer identifier for the requested URL; these mappings are also 1-to-1 and are preserved across the entire data set

size - the number of bytes in the response

method - the method contained in the client's request (e.g., GET).

status - this field contains two pieces of information; the 2 highest order bits contain the HTTP version indicated in the client's request (e.g., HTTP/1.0); the remaining 6 bits indicate the response status code (e.g., 200 OK).

type - the type of file requested (e.g., HTML, IMAGE, etc), generally based on the file extension (.html), or the presence of a parameter list (e.g., '?' indicates a DYNAMIC request). If the url ends with '/', it is considered a DIRECTORY.

server - indicates which server handled the request. The upper 3 bits indicate which region the server was at (e.g., SANTA CLARA, PLANO, HERNDON, PARIS); the remaining bits indicate which server at the site handled the request. All 8 bits can also be used to determine a unique server.

More information on the request structure and its various fields is available in the README contained in the tar file of tools (see below), and reproduced here. The README file also describes how the name of the method, HTTP version, status code, etc are coded in the available bits.

Measurement

During the collection period, there were 33 different World Cup HTTP servers at four geographic locations: Paris, France; Plano, Texas; Herndon, Virginia; and Santa Clara, California. Note that not all servers were in use for the entire collection period. All of the servers recorded timestamps with a 1 second resolution. The time on each server was coordinated with the local time in France (+0200). The first access logs were collected on April 30th, 1998; the final access logs were collected on July 26th, 1998. During this 88 day period, 1,352,804,107 requests were received by the World Cup site. No information is available regarding how many requests were not logged, though it is believed that there were no system outages during the collection period.
Privacy
To ensure the privacy of each individual that visited the World Cup site we have removed all of the client IP addresses and replaced them with a unique integer identifier. The mapping file for this is not publicly available. Otherwise all of the information from the original World Cup access logs is available in the binary log files.
Tools
A set of tools are available to enable researchers to work with the binary log files from the 1998 World Cup Web site. The source code for the tools along with a more complete description of how to use these tools is available in the tool archive.
The three tools provided are:

read: this is a very simple tool that reads each request in a binary log and prints the total number of requests contained in that log. This tool is provided for those who have not worked with binary files before.
checklog: this tool reads the log and calculates a number of high level statistics (e.g., total requests and total bytes transferred). The source code also reveals how to extract the information from each field in the request structure. This tool allows the user to validate that the access logs were transferred correctly and that the tools are functioning properly (for more information on how to do this please see the README file in the tool archive.
recreate: this tool converts the binary log back into the Common Log Format. This tool can generate input for other existing tools which expect this standard data format. This tool also calculates several high level statistics, similar to checklog. However, since this tool converts several of the fields (e.g., objectID and timestamp) it is slower than checklog.
These tools were designed to allow the binary logs to be utilized on both big and little endian platforms. The author offers no guarantee however that the tools will compile or function correctly on all platforms.
Acknowledgements
The 1998 World Cup Web site logs were contributed to the ITA by Martin Arlitt. For inquiries please contact Martin at arlitt@hpl.hp.com. The binary logs, documentation and tools were created by Martin Arlitt with assistance from Tai Jin, Greg Oster and Balachander Krishnamurthy.
You have permission to use and redistribute these access logs freely, as long as this Copyright and Disclaimer is distributed unmodified. If you publish any results based on these access logs, please send us a copy of this publication (in electronic or print form) and give the following reference or attribution in your publication:

M. Arlitt and T. Jin, "1998 World Cup Web Site Access Logs", August 1998. Available at http://www.acm.org/sigcomm/ITA/.
Publications
A technical report describing a workload characterization of these access logs is available from the Hewlett-Packard Labs Web site. The original version of this report was published in February 1999. A revision of this paper was completed in September 1999.
Restrictions
           Copyright (C) 1997, 1998, 1999 Hewlett-Packard Company
                         ALL RIGHTS RESERVED.
 
  The enclosed software and documentation includes copyrighted works
  of Hewlett-Packard Co. For as long as you comply with the following
  limitations, you are hereby authorized to (i) use, reproduce, and
  modify the software and documentation, and to (ii) distribute the
  software and documentation, including modifications, for
  non-commercial purposes only.
      
  1.  The enclosed software and documentation is made available at no
      charge in order to advance the general development of
      the Internet, the World-Wide Web, and Electronic Commerce.
 
  2.  You may not delete any copyright notices contained in the
      software or documentation. All hard copies, and copies in
      source code or object code form, of the software or
      documentation (including modifications) must contain at least
      one of the copyright notices.
 
  3.  The enclosed software and documentation has not been subjected
      to testing and quality control and is not a Hewlett-Packard Co.
      product. At a future time, Hewlett-Packard Co. may or may not
      offer a version of the software and documentation as a product.
  
  4.  THE SOFTWARE AND DOCUMENTATION IS PROVIDED "AS IS".
      HEWLETT-PACKARD COMPANY DOES NOT WARRANT THAT THE USE,
      REPRODUCTION, MODIFICATION OR DISTRIBUTION OF THE SOFTWARE OR
      DOCUMENTATION WILL NOT INFRINGE A THIRD PARTY'S INTELLECTUAL
      PROPERTY RIGHTS. HP DOES NOT WARRANT THAT THE SOFTWARE OR
      DOCUMENTATION IS ERROR FREE. HP DISCLAIMS ALL WARRANTIES,
      EXPRESS AND IMPLIED, WITH REGARD TO THE SOFTWARE AND THE
      DOCUMENTATION. HP SPECIFICALLY DISCLAIMS ALL WARRANTIES OF
      MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
  
  5.  HEWLETT-PACKARD COMPANY WILL NOT IN ANY EVENT BE LIABLE FOR ANY
      DIRECT, INDIRECT, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES
      (INCLUDING LOST PROFITS) RELATED TO ANY USE, REPRODUCTION,
      MODIFICATION, OR DISTRIBUTION OF THE SOFTWARE OR DOCUMENTATION.
Distribution
The tools to work with the binary logs are available in the tool archive. This archive includes a small test access log consisting of 1,000 requests so that users can evaluate the logs and the tools without downloading a large dataset.
The access logs for all servers have been combined into a single sequence of requests, sorted by the recorded timestamp of each request. Due to the volume of data, the binary log has been split into a number of intervals. Each interval represents one day of the overall log, beginning at 0:00:00 local time in Paris and ending at 23:59:59 the same day. In order to keep the size of each log file below 50 MB some of the 1 day intervals needed to be divided into subintervals. In this situation the first (n-1) subintervals each contain 7 million requests while the nth subinterval contains between 1 and 7,000,000 requests.

The log files have the following naming format:

wc_dayX_Y.gz
where:
X is an integer that represents the day the access log was collected
Y is an integer that represents the subinterval for a particular day
Chronological order is determined first by the day of the acces log and second by the subinterval (lower subintervals occur first). For example the following sequence would replay the request sequence for days 79-81 in chronological order:

wc_day79_1.gz
wc_day79_2.gz
wc_day79_3.gz
wc_day79_4.gz
wc_day80_1.gz
wc_day80_2.gz
wc_day81_1.gz
In total there are 249 binary log files for the 92 days during which the access logs were collected (actually no access logs were collected on the first four days; an empty binary log file exists for days 1 through 4). The day of the week can be readily determined from the number assigned to the log file:

if DAY mod 7 = 1 then the log was collected on a Sunday;
if DAY mod 7 = 2 then the log was collected on a Monday;
if DAY mod 7 = 3 then the log was collected on a Tuesday;
if DAY mod 7 = 4 then the log was collected on a Wednesday;
if DAY mod 7 = 5 then the log was collected on a Thursday;
if DAY mod 7 = 6 then the log was collected on a Friday;
if DAY mod 7 = 0 then the log was collected on a Saturday.
For example, wc_day92_1.gz is the log file for day 92; since 92 mod 7 = 1 we know that this log was collected on a Sunday.
The following is a list of all of the available binary log files:

wc_day1_1.gz April 26, 1998 (empty file)
wc_day2_1.gz April 27, 1998 (empty file)
wc_day3_1.gz April 28, 1998 (empty file)
wc_day4_1.gz April 29, 1998 (empty file)
wc_day5_1.gz April 30, 1998
wc_day6_1.gz May 1, 1998
wc_day7_1.gz May 2, 1998
wc_day8_1.gz May 3, 1998
wc_day9_1.gz May 4, 1998
wc_day10_1.gz May 5, 1998
wc_day11_1.gz May 6, 1998
wc_day12_1.gz May 7, 1998
wc_day13_1.gz May 8, 1998
wc_day14_1.gz May 9, 1998
wc_day15_1.gz May 10, 1998
wc_day16_1.gz May 11, 1998
wc_day17_1.gz May 12, 1998
wc_day18_1.gz May 13, 1998
wc_day19_1.gz May 14, 1998
wc_day20_1.gz May 15, 1998
wc_day21_1.gz May 16, 1998
wc_day22_1.gz May 17, 1998
wc_day23_1.gz May 18, 1998
wc_day24_1.gz May 19, 1998
wc_day25_1.gz May 20, 1998
wc_day26_1.gz May 21, 1998
wc_day27_1.gz May 22, 1998
wc_day28_1.gz May 23, 1998
wc_day29_1.gz May 24, 1998
wc_day30_1.gz May 25, 1998
wc_day31_1.gz May 26, 1998
wc_day32_1.gz May 27, 1998
wc_day33_1.gz May 28, 1998
wc_day34_1.gz May 29, 1998
wc_day35_1.gz May 30, 1998
wc_day36_1.gz May 31, 1998
wc_day37_1.gz June 1, 1998
wc_day38_1.gz June 2, 1998
wc_day38_2.gz
wc_day39_1.gz June 3, 1998
wc_day39_2.gz
wc_day40_1.gz June 4, 1998
wc_day40_2.gz
wc_day41_1.gz June 5, 1998
wc_day41_2.gz
wc_day42_1.gz June 6, 1998
wc_day43_1.gz June 7, 1998
wc_day44_1.gz June 8, 1998
wc_day44_2.gz
wc_day44_3.gz
wc_day45_1.gz June 9, 1998
wc_day45_2.gz
wc_day45_3.gz
wc_day46_1.gz June 10, 1998
wc_day46_2.gz
wc_day46_3.gz
wc_day46_4.gz
wc_day46_5.gz
wc_day46_6.gz
wc_day46_7.gz
wc_day46_8.gz
wc_day47_1.gz June 11, 1998
wc_day47_2.gz
wc_day47_3.gz
wc_day47_4.gz
wc_day47_5.gz
wc_day47_6.gz
wc_day47_7.gz
wc_day47_8.gz
wc_day48_1.gz June 12, 1998
wc_day48_2.gz
wc_day48_3.gz
wc_day48_4.gz
wc_day48_5.gz
wc_day48_6.gz
wc_day48_7.gz
wc_day49_1.gz June 13, 1998
wc_day49_2.gz
wc_day49_3.gz
wc_day49_4.gz
wc_day50_1.gz June 14, 1998
wc_day50_2.gz
wc_day50_3.gz
wc_day50_4.gz
wc_day51_1.gz June 15, 1998
wc_day51_2.gz
wc_day51_3.gz
wc_day51_4.gz
wc_day51_5.gz
wc_day51_6.gz
wc_day51_7.gz
wc_day51_8.gz
wc_day51_9.gz
wc_day52_1.gz June 16, 1998
wc_day52_2.gz
wc_day52_3.gz
wc_day52_4.gz
wc_day52_5.gz
wc_day52_6.gz
wc_day53_1.gz June 17, 1998
wc_day53_2.gz
wc_day53_3.gz
wc_day53_4.gz
wc_day53_5.gz
wc_day53_6.gz
wc_day54_1.gz June 18, 1998
wc_day54_2.gz
wc_day54_3.gz
wc_day54_4.gz
wc_day54_5.gz
wc_day54_6.gz
wc_day55_1.gz June 19, 1998
wc_day55_2.gz
wc_day55_3.gz
wc_day55_4.gz
wc_day55_5.gz
wc_day56_1.gz June 20, 1998
wc_day56_2.gz
wc_day56_3.gz
wc_day57_1.gz June 21, 1998
wc_day57_2.gz
wc_day57_3.gz
wc_day58_1.gz June 22, 1998
wc_day58_2.gz
wc_day58_3.gz
wc_day58_4.gz
wc_day58_5.gz
wc_day58_6.gz
wc_day59_1.gz June 23, 1998
wc_day59_2.gz
wc_day59_3.gz
wc_day59_4.gz
wc_day59_5.gz
wc_day59_6.gz
wc_day59_7.gz
wc_day60_1.gz June 24, 1998
wc_day60_2.gz
wc_day60_3.gz
wc_day60_4.gz
wc_day60_5.gz
wc_day60_6.gz
wc_day60_7.gz
wc_day61_1.gz June 25, 1998
wc_day61_2.gz
wc_day61_3.gz
wc_day61_4.gz
wc_day61_5.gz
wc_day61_6.gz
wc_day61_7.gz
wc_day61_8.gz
wc_day62_1.gz June 26, 1998
wc_day62_2.gz
wc_day62_3.gz
wc_day62_4.gz
wc_day62_5.gz
wc_day62_6.gz
wc_day62_7.gz
wc_day62_8.gz
wc_day62_9.gz
wc_day62_10.gz
wc_day63_1.gz June 27, 1998
wc_day63_2.gz
wc_day63_3.gz
wc_day63_4.gz
wc_day64_1.gz June 28, 1998
wc_day64_2.gz
wc_day64_3.gz
wc_day65_1.gz June 29, 1998
wc_day65_2.gz
wc_day65_3.gz
wc_day65_4.gz
wc_day65_5.gz
wc_day65_6.gz
wc_day65_7.gz
wc_day65_8.gz
wc_day65_9.gz
wc_day66_1.gz June 30, 1998
wc_day66_2.gz
wc_day66_3.gz
wc_day66_4.gz
wc_day66_5.gz
wc_day66_6.gz
wc_day66_7.gz
wc_day66_8.gz
wc_day66_9.gz
wc_day66_10.gz
wc_day66_11.gz
wc_day67_1.gz July 1, 1998
wc_day67_2.gz
wc_day67_3.gz
wc_day67_4.gz
wc_day67_5.gz
wc_day68_1.gz July 2, 1998
wc_day68_2.gz
wc_day68_3.gz
wc_day69_1.gz July 3, 1998
wc_day69_2.gz
wc_day69_3.gz
wc_day69_4.gz
wc_day69_5.gz
wc_day69_6.gz
wc_day69_7.gz
wc_day70_1.gz July 4, 1998
wc_day70_2.gz
wc_day70_3.gz
wc_day71_1.gz July 5, 1998
wc_day71_2.gz
wc_day72_1.gz July 6, 1998
wc_day72_2.gz
wc_day72_3.gz
wc_day73_1.gz July 7, 1998
wc_day73_2.gz
wc_day73_3.gz
wc_day73_4.gz
wc_day73_5.gz
wc_day73_6.gz
wc_day74_1.gz July 8, 1998
wc_day74_2.gz
wc_day74_3.gz
wc_day74_4.gz
wc_day74_5.gz
wc_day74_6.gz
wc_day75_1.gz July 9, 1998
wc_day75_2.gz
wc_day75_3.gz
wc_day76_1.gz July 10, 1998
wc_day76_2.gz
wc_day77_1.gz July 11, 1998
wc_day77_2.gz
wc_day78_1.gz July 12, 1998
wc_day78_2.gz
wc_day79_1.gz July 13, 1998
wc_day79_2.gz
wc_day79_3.gz
wc_day79_4.gz
wc_day80_1.gz July 14, 1998
wc_day80_2.gz
wc_day81_1.gz July 15, 1998
wc_day82_1.gz July 16, 1998
wc_day83_1.gz July 17, 1998
wc_day84_1.gz July 18, 1998
wc_day85_1.gz July 19, 1998
wc_day86_1.gz July 20, 1998
wc_day87_1.gz July 21, 1998
wc_day88_1.gz July 22, 1998
wc_day89_1.gz July 23, 1998
wc_day90_1.gz July 24, 1998
wc_day91_1.gz July 25, 1998
wc_day92_1.gz July 26, 1998


Up to Traces In The Internet Traffic Archive.
