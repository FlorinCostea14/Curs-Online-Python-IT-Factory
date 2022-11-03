public class Tema_Curs_Primii_Pasi_In_Programare {
    // 3.
    public static void main(String[] args) {
        String marcaMasina = "Audi Q5";
        System.out.println("Am cumparat o masina marca: " + marcaMasina);

        Integer an_fabricatie = 2014;
        System.out.println("Masina" + " " +  marcaMasina + " " + "este fabricata in anul" + " " + an_fabricatie);

        Double pret = 25500.50;
        System.out.println("Masina" + " " + marcaMasina + " " + "a avut pretul de" + " " + pret + " " + "euro.");

        Boolean inmatriculata = true;
        if (inmatriculata == true)
            System.out.println("Masina este inmatriculata.");
        else if (inmatriculata == false)
            System.out.println("Masina nu este inmatriculata");

        // 5.
        int i;
        for (i=1; i<20; i = i+3)
            System.out.println( i );


    }
}
// 1.
/* O variabila boolean este un tip de date folosit
pentru a identifica daca o informatie este adevarata sau falsa
 */

