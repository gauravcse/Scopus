/*** 	CREATED BY GAURAV MITRA ***/	


/*** A SIMPLE PARSER WRITTEN IN JAVA FOR PARSING THE SCRAPED DATA FROM SCOPUS DATABASE ***/
/*** WRITES THE DATA TO A FILE ***/


import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;



public class Parser {
	public static void main(String args[])throws IOException {
		File file1 = new File("database.txt");
		File file2 = new File("format_database.txt");
		FileOutputStream fos = new FileOutputStream(file2);
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(fos));
		FileInputStream fis = new FileInputStream(file1);
		BufferedReader br = new BufferedReader(new InputStreamReader(fis));
		String line = null;
		ArrayList<String> document = new ArrayList<String>();
		ArrayList<String> topic = new ArrayList<String>();
		ArrayList<String> paper = new ArrayList<String>();
		while((line = br.readLine()) != null) {
			String array[] = line.split(",");
			document.add(array[array.length - 1]);
			topic.add(array[array.length - 4]);
			int len = (array[array.length-1] + array[array.length-2] + array[array.length-3] + array[array.length-4]).length(); 
			paper.add(line.substring(2,(line.length() - len -2)).trim());
		}
		br.close();
		fis.close();
		ArrayList<String> doi = new ArrayList<String>();
		ArrayList<String> cite = new ArrayList<String>();
		ArrayList<String> date = new ArrayList<String>();
		for(String docs : document) {
			docs = docs.trim();
			doi.add(docs.substring((docs.indexOf(" ")+5),(docs.indexOf(" ",(docs.indexOf(" ")+4)))));
			String ci = (docs.substring(docs.lastIndexOf("(")+1, docs.lastIndexOf(")"))).trim();
			cite.add(ci.substring(ci.indexOf(" "),ci.lastIndexOf(" ")));
			date.add(docs.substring(docs.indexOf("(")+1,docs.indexOf(")")));
		}
		for(int i = 0; i<topic.size(); i++) {
			String data = doi.get(i)+"\t"+cite.get(i)+"\t"+date.get(i)+"\t"+(paper.get(i).substring(0,paper.get(i).length()-1));
			bw.write(data+"\n");
		}
		bw.close();
		fos.close();
	}
}
