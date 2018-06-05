import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class FileReader {

	static String algoritmo = "WIN_1000";
	static String diretorio = "/home/athos/Documentos/github/support-masters/raw_data/" + algoritmo + "/";
	static String nomeArquivo = "mk_4_incremental_drift";

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
					newLine = newLine.replace(".", ",");
					gravarArquivo(newLine);
					

				}		       	


			}
			
			scanner.close();

		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
	}

	/*
	 * Metodo que acessa uma subpasta e realizada a chamada para o metodo de leitura para cada arquivo
	 *
	 */
	public static void listFilesForFolder(final File folder) {
		String[] caminhoSeparado;
		int contador = 0;
		

		for (final File fileEntry : folder.listFiles()) {
			if (fileEntry.isDirectory()) {
				listFilesForFolder(fileEntry);
			} else {

				if(fileEntry.getPath().contains(nomeArquivo)) {
					lerArquivo(fileEntry.getPath());
				}

			}
		}


	}


	public static void main(String[] args) {
		final File folder = new File(diretorio);
		
		listFilesForFolder(folder);
			

	}

}
