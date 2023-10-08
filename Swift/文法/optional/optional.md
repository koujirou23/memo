### outletのOptional型について
https://qiita.com/Lulu34/items/791ad052a6dce480175c  

### Optional型について

!、?の解説  
https://qiita.com/maiki055/items/b24378a3707bd35a31a8  
オプショナル型は変数を宣言時の"!"と"?"のことを言う  
宣言をした段階では、nilが入る  
  
変数宣言以外での"!"と"?"は アンラップの意味  
アンラップしなければ、optional(値)という値が出力されてしまう  
　　
・強制アンラップ "!"  
オプショナル型変数の後ろに"!"をつける  
※アンラップ対象のオプショナル型の変数の中身がnillの場合は、エラーとなりアプリが落ちてしまう  
```
var optional: Int? = 10
println(optional) // → Optional(10)
println(optional!) // → 10
```
  
・オプショナルバインディング  
if文などの条件式と組み合わせて使う  
```
var hobby: String? // オプショナル型

if let unwrappedHobby = hobby {
    println(unwrappedHobby)
}
else {
    println("趣味はありません")
}
```
・オプショナルチェイニング  
オプショナル型変数の後ろに"?"をつける  
```
【例】
オプショナル型の変数?.プロパティ
オプショナル型の変数?.メソッド()
```
  
・「??」??演算子(nil合体演算子)のアンラップ  
もしその値がnilだった場合、代用の値を使うというイメージです。なので、以下のコードは、もしstrがnilだった場合、"代用"という文字列が表示されます。上記の強制アンラップを使うよりなら、こちらの方を使った方が安全です。  
https://ios-docs.dev/swift-optional/#nil  
```
struct ContentView: View {
    var str: String? = "こんにちは"
    
    var body: some View {
        Text(textStr())
            .padding()
    }
    
    func textStr() -> String {
        return str ?? "代用"
    }
}
```  
  
・if letを使ったアンラップ  
以下のプログラムは、strをsに代入してみてsがnilじゃなかったら、Textでsを表示します。もしsがnilだったらif文内の処理は行いません。つまりTextが表示されません。  
このif let文は、strをsに代入してみて、nilじゃない場合に中の処理を実行するというアンラップ方法です。  
nilじゃなかった場合は、そもそも処理を実行しないので、上記の??演算子よりも親切で安全なコードになります。  
```
struct ContentView: View {
    var str: String? = "こんにちは"
    
    var body: some View {
        if let s = str {
            Text(s)
                .padding()
        }
    }
}
```