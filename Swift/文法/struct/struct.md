### 構造体（struct）の内容を変更するメソッド
構造体の定義では、インスタンスの内容を変更するメソッドは、定義の先頭のfuncの直前にmutatingというキーワードを置 かなければなりません。これによって、インスタンスの値を変更するメソッドをコンパイル時に知ることができ、定数に格納さ  れたインスタンスに対する呼び出しを禁止できるほか、効率の良い実行コードが生成できます。  
荻原 剛志. 詳解 Swift 第5版 (Japanese Edition) (p.149). Kindle 版.   

・タイプメソッド  
上で、構造体のインスタンスに対して適用されるメソッドの定義方法を述べました。これらのメソッドはインスタンスの持つ機能や属性を実装するものであり、多くのオブジェクト指向言語における、クラスのインスタンスメソッドに相当すると考えることができます。同様に、クラスメソッドに相当する関数を構造体の内部に定義することができます。これを構造体のタイプメソッド（typemethod）、あるいは静的メソッドと呼びます。タイプメソッドは個々のインスタンスの機能を実装するものではなく、全インスタンスから共通して利用される機能、インスタンスの作り方（個数の制限や再利用）、あるいはその型を使う上で便利な機能などを記述します。タイプメソッドの定義には、関数定義の先頭にstaticというキーワードを付けます。
荻原 剛志. 詳解 Swift 第5版 (Japanese Edition) (pp.150-151). Kindle 版. 

##### 構造体の定義例  
```
struct SimpleDate {
    var year,month,day: Int 
    static func isLeap(_y:Int) -> Bool { //タイプメソッド
        return (y % 4 == 0) && (y % 100 !=0 || y % 400 == 0) 
    }
    static func daysOfMonth(_m:Int,year:Int) -> Int {
        switch m {
            case 2 :return isLeap(year) ? 29 : 28 //Self.isLeapでも同じ
            case 4,6,9,11: return30 
            default: return31
            }
        }    
    func leapYear() -> Bool {
        SimpleDate.isLeap(year) //型名またはSelfが必要
        }
    }

// 呼び出し例
SimpleDate.isLeap(2000)                        //trueが返る
SimpleDate.daysOfMonth(2, year:2000)           //29が返る
let d = SimpleDate(year:2024, month:11, day:7)
print("うるう年? ",d.leapYear())                //trueが返る

// 荻原 剛志. 詳解 Swift 第5版 (Japanese Edition) (pp.151-152). Kindle 版. 
```