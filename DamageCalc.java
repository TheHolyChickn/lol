import java.util.Scanner;
import java.util.ArrayList;
  //note - variables are initiated for gdrag values as this program was initially only for edrag, i added some code to allow for other pets later
class DamageCalc {
  //initiating variables
  public static double dmg = 5;
  public static double str;
  public static double cd;
  public static double intel;
  public static double addBuffs = 5.6;
  public static double strAddBuffs = 1.05;
  public static double cdAddBuffs = 1;
  public static int powerLVL;
  public static int stoneLVL;
  public static int timeLVL;
  public static ArrayList<Double> multiBuffs = new ArrayList<Double>();
  public static ArrayList<Double> strMultiBuffs = new ArrayList<Double>();
  public static ArrayList<Double> cdMultiBuffs = new ArrayList<Double>();
  
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    String temp = "";
    int temp2;
    double temp3;
    double def;
    double damage;

    //pet
   System.out.println("What pet are you using? Enter '1' for gdrag, '2' for edrag, or '3' for manual input. Gdrag assumes 50+ magic find & 1b bank. Edrag does NOT assume end mob.");
    temp2 = input.nextInt();
    if(temp2 == 1){
      //owo
    }
    else if(temp2 == 2){
      addBuffs = 3.1;
      strAddBuffs = 1.1;
      cdAddBuffs = 1.1;
    }
    else{
      addBuffs = 3.1;
      strAddBuffs = 1.0;
    }
    System.out.println(addBuffs + ", " + strAddBuffs + ", " + cdAddBuffs + "**THIS IS A DEBUG MESSAGE**\n");
    
    //damage
    System.out.println("Enter your item's damage");
    dmg += input.nextDouble();
    System.out.println("Enter your arrow's damage");
    dmg += input.nextDouble();

    //strength
    System.out.println("Enter your strength pre-multipliers and pre-blesssings");
    str += input.nextDouble();

    //crit damage
    System.out.println("Enter your crit damage pre-multipliers and pre-blessings");
    cd += input.nextDouble();

    //intelligence
    System.out.println("Are you mage? Answer 1 for yes or anything else for no.");
    if(input.nextInt()==1){
      System.out.println("Enter your intelligence pre-multipliers and pre-blessings");
      intel += input.nextDouble();
    }

    //power blessing
    System.out.println("Enter power blessing lvl");
    powerLVL = input.nextInt();
    convertPower(powerLVL);

    //stone blessing
    System.out.println("Enter stone blessing lvl");
    stoneLVL = input.nextInt();
    convertStone(stoneLVL);

    //time blessing
    System.out.println("Enter time blessing lvl");
    timeLVL = input.nextInt();
    convertTime(timeLVL);

    //additive buffs
    System.out.println("Enter every additive buff, pressing enter between each one. Enter 0 when you are finished. Do not enter combat level or gdrag buffs.");
    temp3 = input.nextDouble();
    while(temp3 != 0){
      addBuffs += temp3;
      temp3 = input.nextDouble();
    }

    //multiplicative buffs
    System.out.println("Enter every multiplicative buff, pressing enter between each one. Enter 0 when you are finished.");
    temp3 = input.nextDouble();
    while(temp3 != 0){
      multiBuffs.add(temp3);
      temp3 = input.nextDouble();
    }

    //additive strength buffs
    System.out.println("Enter every additive strength buff, pressing enter between each one. Enter 0 when you are finished. Do not enter gdrag buffs.");
    temp3 = input.nextDouble();
    while(temp3 != 0){
      strAddBuffs += temp3;
      temp3 = input.nextDouble();
    }

    //multiplicative strength buffs
    System.out.println("Enter every multiplicative strength buff, pressing enter between each one. Enter 0 when you are finished.");
    temp3 = input.nextDouble();
    while(temp3 != 0){
      strMultiBuffs.add(temp3);
      temp3 = input.nextDouble();
    }

    //additive crit damage buffs
    System.out.println("Enter every additive crit damage buff, pressing enter between each one. Enter 0 when you are finished.");
    temp3 = input.nextDouble();
    while(temp3 != 0){
      cdAddBuffs += temp3;
      temp3 = input.nextDouble();
    }

    //multiplicative crit damage buffs
    System.out.println("Enter every multiplicative crit damage buff, pressing enter between each one. Enter 0 when you are finished.");
    temp3 = input.nextDouble();
    while(temp3 != 0){
      cdMultiBuffs.add(temp3);
      temp3 = input.nextDouble();
    }
    //damage resistance
    System.out.println("Enter the mob's defense");
    def = input.nextDouble();
    def = 1 - (def/(def + 100));

    //calculating final str
    str = str * strAddBuffs;
    if(strMultiBuffs.size() > 0){
      for(int i = 0; i < strMultiBuffs.size(); i++){
        str *= strMultiBuffs.get(i);
      }
    }
    
    //calculating final cd
    cd = cd * cdAddBuffs;
    if(cdMultiBuffs.size() > 0){
      for(int i = 0; i < cdMultiBuffs.size(); i++){
        cd *= cdMultiBuffs.get(i);
      }
    }
    
    //calculating theoretical dmg
    damage = dmg * (1 + (str / 100)) * (1 + (cd / 100)) * addBuffs;
    if(multiBuffs.size() > 0){
      for(int i = 0; i < multiBuffs.size(); i++){
        damage *= multiBuffs.get(i);
      }
    }
    damage *= def;
    System.out.println(damage);
  }
  
  //blessing thingys
  public static void convertPower(int power){
    double flatBuff = 1.1 * 1.2 * 4 * power;
    str += flatBuff;
    cd += flatBuff;
    double multiBuff = 1 + (1.1 * 1.2 * 0.02 * power);
    strMultiBuffs.add(multiBuff);
    cdMultiBuffs.add(multiBuff);
  }
  public static void convertStone(int stone){
    double flatBuff = 1.1 * 1.2 * 6 * stone;
    dmg += flatBuff;
  }
  public static void convertTime(int time){
    double flatBuff = 1.1 * 1.2 * 4 * time;
    str += flatBuff;
    double multiBuff = 1 + (1.1 * 1.2 * 0.02 * time);
    strMultiBuffs.add(multiBuff);
  }
}