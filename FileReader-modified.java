import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class FileReader {

	static String algoritmo = "WIN_10";
	static String diretorio = "/home/athos/Documentos/github/support-masters/raw_data/" + algoritmo + "/";
	static String nomeArquivo;//= "ofs_100_spam_data";
	static double[][] medias;
	static int fileType = 0; // 0 none; 1 - 100k (others); 2 - 9324 (spam_data); 3- 5995 (mailing_list)
	static int rowLength=0, colLength =0;
	
	
	/*
	 * Metodo que converte uma lista de strings para uma lista de floats
	 */
	public static List<Float> stringToFloat (String[] valoresSeparados) {
		List<Float> valores = new ArrayList<Float>();

		for(int i=0;i<valoresSeparados.length;i++) {
			valores.add(Float.parseFloat(valoresSeparados[i]));

		}	
		return valores;
	}



	/*
	 * Metodo que grava uma amostra em um arquivo arff a partir de uma lista de strings. IMPORTANTE: existe sobrecarga neste metodo, pois outro metodo com o mesmo nome
	 * ja existe nesta classe.
	 */
	public static void gravarArquivo(String linha){

		BufferedWriter outputWriter = null;
		String nomeArquivoCompilado = diretorio + nomeArquivo +"_compiled.ods";

		try {

			File file = new File(nomeArquivoCompilado);

			outputWriter = new BufferedWriter(new FileWriter(nomeArquivoCompilado, true));
			outputWriter.write(linha);
			outputWriter.newLine();

			outputWriter.flush();  
			outputWriter.close();  


		} catch (Exception ex) {
			ex.printStackTrace();
		}

	}
	
	public static void gravarArquivo(double[][] medias){

		BufferedWriter outputWriter = null;
		String nomeArquivoCompilado = diretorio + nomeArquivo +"_compiled.ods";

		try {

			File file = new File(nomeArquivoCompilado);

			outputWriter = new BufferedWriter(new FileWriter(nomeArquivoCompilado, true));
			outputWriter.newLine();
			
			outputWriter.write("Quantidade");
			outputWriter.write(";");
			outputWriter.write("Tempo");
			outputWriter.write(";");
			outputWriter.write("RAM");
			outputWriter.write(";");
			outputWriter.write("ACC");
			outputWriter.newLine();
			
			for(int i=0; i<rowLength; i++) {
				for(int j =0; j<colLength; j++) {
					 
					outputWriter.write(String.valueOf(medias[i][j]));
					outputWriter.write(";");
				}
				outputWriter.newLine();
			}
			
			outputWriter.newLine();
			
			for(int k=1; k<4;k++) {
				
				switch(k) {
				case 1:
					outputWriter.write("Tempo");
					break;
				case 2:
					outputWriter.write("RAM");
					break;
				case 3:
					outputWriter.write("ACC");
					break;
				}
				
				outputWriter.write(";");
				
				for(int i=0; i<rowLength;i++) {	
					//se for o ultimo, nao adiciona a virgula
					if(i==rowLength-1) {
						outputWriter.write(String.valueOf(medias[i][k]));				
					} else {
						outputWriter.write(String.valueOf(medias[i][k]) + ",");				
					}
									
				}
				outputWriter.newLine();
				
			}
			
			
			outputWriter.newLine();

			outputWriter.flush();  
			outputWriter.close();  


		} catch (Exception ex) {
			ex.printStackTrace();
		}

	}
	
	public static void calculaMedia() {
		
		for(int i =0; i<rowLength; i++) {
			for(int j=0; j<colLength; j++) {
				//se nao for a primeira coluna de cada linha, que contem o header
				if(j!=0) {
					medias[i][j] = medias[i][j] / 10;
				}
				
			}
		}
		
	}
	
	public static void inicializaMediaArtificial(String[] stringSplit) {
		if(stringSplit[0].equals("10000.0")) {
		  	medias[0][0] += 10000.00;
		  	medias[0][1] += Double.parseDouble(stringSplit[1]);
		  	medias[0][2] += Double.parseDouble(stringSplit[2]);
		  	medias[0][3] += Double.parseDouble(stringSplit[4]);
	  }
	  else if(stringSplit[0].equals("20000.0")) {
		    medias[1][0] += 20000.00;
		  	medias[1][1] += Double.parseDouble(stringSplit[1]);
		  	medias[1][2] += Double.parseDouble(stringSplit[2]);
		  	medias[1][3] += Double.parseDouble(stringSplit[4]);
	  }
	  else if(stringSplit[0].equals("30000.0")) {
		    medias[2][0] += 30000.00;
		  	medias[2][1] += Double.parseDouble(stringSplit[1]);
		  	medias[2][2] += Double.parseDouble(stringSplit[2]);
		  	medias[2][3] += Double.parseDouble(stringSplit[4]);
	  }
	  else if(stringSplit[0].equals("40000.0")) {
		    medias[3][0] += 40000.00;
		  	medias[3][1] += Double.parseDouble(stringSplit[1]);
		  	medias[3][2] += Double.parseDouble(stringSplit[2]);
		  	medias[3][3] += Double.parseDouble(stringSplit[4]);
	  }
	  else if(stringSplit[0].equals("50000.0")) {
		    medias[4][0] += 50000.00;
		  	medias[4][1] += Double.parseDouble(stringSplit[1]);
		  	medias[4][2] += Double.parseDouble(stringSplit[2]);
		  	medias[4][3] += Double.parseDouble(stringSplit[4]);
	  }
	  else if(stringSplit[0].equals("60000.0")) {
		    medias[5][0] += 60000.00;
		  	medias[5][1] += Double.parseDouble(stringSplit[1]);
		  	medias[5][2] += Double.parseDouble(stringSplit[2]);
		  	medias[5][3] += Double.parseDouble(stringSplit[4]);
	  }
	  else if(stringSplit[0].equals("70000.0")) {
		    medias[6][0] += 70000.00;
		  	medias[6][1] += Double.parseDouble(stringSplit[1]);
		  	medias[6][2] += Double.parseDouble(stringSplit[2]);
		  	medias[6][3] += Double.parseDouble(stringSplit[4]);
	  }
	  else if(stringSplit[0].equals("80000.0")) {
		    medias[7][0] += 80000.00;
		  	medias[7][1] += Double.parseDouble(stringSplit[1]);
		  	medias[7][2] += Double.parseDouble(stringSplit[2]);
		  	medias[7][3] += Double.parseDouble(stringSplit[4]);
	  }
	  else if(stringSplit[0].equals("90000.0")) {
		    medias[8][0] += 90000.00;
		  	medias[8][1] += Double.parseDouble(stringSplit[1]);
		  	medias[8][2] += Double.parseDouble(stringSplit[2]);
		  	medias[8][3] += Double.parseDouble(stringSplit[4]);
	  }
	  else if(stringSplit[0].equals("100000.0")) {
		    medias[9][0] += 100000.00;
		  	medias[9][1] += Double.parseDouble(stringSplit[1]);
		  	medias[9][2] += Double.parseDouble(stringSplit[2]);
		  	medias[9][3] += Double.parseDouble(stringSplit[4]);
	  }
		
	}
	
	public static void inicializaMediaSpamData(String[] stringSplit) {
		 if(stringSplit[0].equals("1000.0")) {
			  	medias[0][0] += 1000.00;
			  	medias[0][1] += Double.parseDouble(stringSplit[1]);
			  	medias[0][2] += Double.parseDouble(stringSplit[2]);
			  	medias[0][3] += Double.parseDouble(stringSplit[4]);
		  }
		  else if(stringSplit[0].equals("2000.0")) {
			    medias[1][0] += 2000.00;
			  	medias[1][1] += Double.parseDouble(stringSplit[1]);
			  	medias[1][2] += Double.parseDouble(stringSplit[2]);
			  	medias[1][3] += Double.parseDouble(stringSplit[4]);
		  }
		  else if(stringSplit[0].equals("3000.0")) {
			    medias[2][0] += 3000.00;
			  	medias[2][1] += Double.parseDouble(stringSplit[1]);
			  	medias[2][2] += Double.parseDouble(stringSplit[2]);
			  	medias[2][3] += Double.parseDouble(stringSplit[4]);
		  }
		  else if(stringSplit[0].equals("4000.0")) {
			    medias[3][0] += 4000.00;
			  	medias[3][1] += Double.parseDouble(stringSplit[1]);
			  	medias[3][2] += Double.parseDouble(stringSplit[2]);
			  	medias[3][3] += Double.parseDouble(stringSplit[4]);
		  }
		  else if(stringSplit[0].equals("5000.0")) {
			    medias[4][0] += 5000.00;
			  	medias[4][1] += Double.parseDouble(stringSplit[1]);
			  	medias[4][2] += Double.parseDouble(stringSplit[2]);
			  	medias[4][3] += Double.parseDouble(stringSplit[4]);
		  }
		  else if(stringSplit[0].equals("6000.0")) {
			    medias[5][0] += 6000.00;
			  	medias[5][1] += Double.parseDouble(stringSplit[1]);
			  	medias[5][2] += Double.parseDouble(stringSplit[2]);
			  	medias[5][3] += Double.parseDouble(stringSplit[4]);
		  }
		  else if(stringSplit[0].equals("7000.0")) {
			    medias[6][0] += 7000.00;
			  	medias[6][1] += Double.parseDouble(stringSplit[1]);
			  	medias[6][2] += Double.parseDouble(stringSplit[2]);
			  	medias[6][3] += Double.parseDouble(stringSplit[4]);
		  }
		  else if(stringSplit[0].equals("8000.0")) {
			    medias[7][0] += 8000.00;
			  	medias[7][1] += Double.parseDouble(stringSplit[1]);
			  	medias[7][2] += Double.parseDouble(stringSplit[2]);
			  	medias[7][3] += Double.parseDouble(stringSplit[4]);
		  }
		  else if(stringSplit[0].equals("9000.0")) {
			    medias[8][0] += 9000.00;
			  	medias[8][1] += Double.parseDouble(stringSplit[1]);
			  	medias[8][2] += Double.parseDouble(stringSplit[2]);
			  	medias[8][3] += Double.parseDouble(stringSplit[4]);
		  }
		  else if(stringSplit[0].equals("9324.0")) {
			    medias[9][0] += 9324.00;
			  	medias[9][1] += Double.parseDouble(stringSplit[1]);
			  	medias[9][2] += Double.parseDouble(stringSplit[2]);
			  	medias[9][3] += Double.parseDouble(stringSplit[4]);
		  }
		
	
	}
	
	public static void inicializaMediaMailingList(String[] stringSplit) {
		if(stringSplit[0].equals("1000.0")) {
		  	medias[0][0] += 1000.00;
		  	medias[0][1] += Double.parseDouble(stringSplit[1]);
		  	medias[0][2] += Double.parseDouble(stringSplit[2]);
		  	medias[0][3] += Double.parseDouble(stringSplit[4]);
	  }
	  else if(stringSplit[0].equals("2000.0")) {
		    medias[1][0] += 2000.00;
		  	medias[1][1] += Double.parseDouble(stringSplit[1]);
		  	medias[1][2] += Double.parseDouble(stringSplit[2]);
		  	medias[1][3] += Double.parseDouble(stringSplit[4]);
	  }
	  else if(stringSplit[0].equals("3000.0")) {
		    medias[2][0] += 3000.00;
		  	medias[2][1] += Double.parseDouble(stringSplit[1]);
		  	medias[2][2] += Double.parseDouble(stringSplit[2]);
		  	medias[2][3] += Double.parseDouble(stringSplit[4]);
	  }
	  else if(stringSplit[0].equals("4000.0")) {
		    medias[3][0] += 4000.00;
		  	medias[3][1] += Double.parseDouble(stringSplit[1]);
		  	medias[3][2] += Double.parseDouble(stringSplit[2]);
		  	medias[3][3] += Double.parseDouble(stringSplit[4]);
	  }
	  else if(stringSplit[0].equals("5000.0")) {
		    medias[4][0] += 5000.00;
		  	medias[4][1] += Double.parseDouble(stringSplit[1]);
		  	medias[4][2] += Double.parseDouble(stringSplit[2]);
		  	medias[4][3] += Double.parseDouble(stringSplit[4]);
	  }
	  else if(stringSplit[0].equals("5995.0")) {
		    medias[5][0] += 5995.00;
		  	medias[5][1] += Double.parseDouble(stringSplit[1]);
		  	medias[5][2] += Double.parseDouble(stringSplit[2]);
		  	medias[5][3] += Double.parseDouble(stringSplit[4]);
	  }
	}

	/*
	 * Metodo que le um arquivo, adiciona seus valores nos respectivos arrays e realiza a chamada do metodo para 
	 * aplicacao dos calculos necessarios em cada amostra
	 */
	public static void lerArquivo(String filename) {

		File file = new File(filename);	
		Scanner scanner;
				

		try {
			scanner = new Scanner(file);
			String lineFromFile;
			while (scanner.hasNextLine()) {
				lineFromFile = scanner.nextLine();
				if(!lineFromFile.contains("learning evaluation")) { 
					String newLine = lineFromFile.replace(",", ";");					
					String stringSplit[] = newLine.split(";");

					switch(fileType) {
						case 1:
							inicializaMediaArtificial(stringSplit);
						  break;
						case 2:
							inicializaMediaSpamData(stringSplit);
						  break;
						case 3:
							inicializaMediaMailingList(stringSplit);
						break;
							
					}

					//newLine = newLine.replace(".", ",");
					//gravarArquivo(newLine);					

				}		       	

			}
			
			scanner.close();

		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
	}

	public static void initializeMedias() {

		if(nomeArquivo.contains("gradual") || nomeArquivo.contains("incremental") || nomeArquivo.contains("recurrent") || nomeArquivo.contains("sudden")) {
			fileType = 1;
		} else if(nomeArquivo.contains("spam")) {
			fileType = 2;
		} else {
			fileType = 3;
		}
		
		switch(fileType) {
			case 1:
				rowLength = 10;
				colLength = 4;
				medias = new double[rowLength][colLength];
			  break;
			 case 2:
				 rowLength = 10;
				 colLength = 4;
				 medias = new double[rowLength][colLength];
			  break;
			 case 3:
				 rowLength = 6;
				 colLength = 4;
				 medias = new double[rowLength][colLength];
			  break;
			 default:
			  break;
		}
		
		for(int i=0; i<rowLength; i++) {
			for(int j=0; j<colLength; j++) {
				medias[i][j] = 0.0;
			}
		}

	}

	/*
	 * Metodo que acessa uma subpasta e realizada a chamada para o metodo de leitura para cada arquivo
	 *
	 */
	public static void listFilesForFolder(final File folder) {
		String[] caminhoSeparado;
		int contador = 0;
		
		initializeMedias();

		for (final File fileEntry : folder.listFiles()) {
			if (fileEntry.isDirectory()) {
				listFilesForFolder(fileEntry);
			} else {

				if(fileEntry.getPath().contains(nomeArquivo)) {
					lerArquivo(fileEntry.getPath());
				}

			}
		}
		calculaMedia();
		gravarArquivo(medias);


	}


	public static void main(String[] args) {
		final File folder = new File(diretorio);
		String algoritmo="ofs";
		
		for(int i=0; i<10;i++) {
			switch(i) {
			case 0:
				nomeArquivo=algoritmo + "_4_" + "spam_data";
				break;
			case 1:
				nomeArquivo=algoritmo + "_10_" + "spam_data";
				break;
			case 2:
				nomeArquivo=algoritmo + "_100_" + "spam_data";
				break;
			case 3:
				nomeArquivo=algoritmo + "_4_" + "mailing_list";
				break;
			case 4:
				nomeArquivo=algoritmo + "_10_" + "mailing_list";
				break;
			case 5:
				nomeArquivo=algoritmo + "_100_" + "mailing_list";
				break;
			case 6:
				nomeArquivo=algoritmo + "_4_" + "sudden_drift";
				break;
			case 7:
				nomeArquivo=algoritmo + "_4_" + "recurrent_drift";
				break;
			case 8:
				nomeArquivo=algoritmo + "_4_" + "gradual_drift";
				break;
			case 9:
				nomeArquivo=algoritmo + "_4_" + "incremental_drift";
				break;
			}
			listFilesForFolder(folder);
		}
	
		
		
	
			

	}

}
