:'
转置文件
给定一个文件 file.txt，转置它的内容。

你可以假设每行列数相同，并且每个字段由 ' ' 分隔。

 

示例：

假设 file.txt 文件内容如下：

name age
alice 21
ryan 30
应当输出：

name alice ryan
age 21 30

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/transpose-file
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'
# 主要使用awk，将文件内容存储到二维数组中，然后再换一种方式输出
 cat file.txt | awk 'BEGIN{c=0;} {for(i=1;i<=NF;i++) {num[c,i] = $i;} c++;} END{ for(i=1;i<=NF;i++){str=""; for(j=0;j<NR;j++){ if(j>0){str = str" "} str= str""num[j,i]}printf("%s\n", str)} }' 
 