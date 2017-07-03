
public Boolean CharIsUnique(String string) {
	//create an BooArray of Booleans, based on AICCI code
	Boolean[] booArray = new Boolean[128];


	//Convert each ch in the string to int as key to BooArray
	for (i=0; i++; i<string.length) {
		char ch = string.charAt(i);
		int hexVal = int(ch);

	//check if the value of BooArray[int] is true or false.
	//if it's true, that means this character exists. Then return false.

		if booArray[hexVal] == true {
			System.out.println("hexValue: " + hexVal);
			return false;
		} else {

		//if it's false,  it hasn't occurred. Set to true.
			booArray[hexVal] = true;
		}

	}
	return true;

}

public static void main(String[] args){
	Scanner scan = new Scanner(System.in);
	string = scanner.toString;
    CharIsUnique(string);

}

