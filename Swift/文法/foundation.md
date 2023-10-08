### Swiftのクラスの概念
https://qiita.com/Kenta-Okuda/items/733ecafbf67dfd5ad9ea#2-%E3%82%A4%E3%83%B3%E3%82%B9%E3%82%BF%E3%83%B3%E3%82%B9%E5%8C%96  
・オーバーロード：引数の数が違うメソッドのこと  
・オーバーライド：スーパークラス（親クラス）に定義されているメソッドをサブクラス（子クラス）で再宣言する  
関数の先頭に override を記述する必要がある
```
override func sample()
```

### 関数定義の基本
返り値の型指定可能  
値を返さない関数は下記のどれか  
1.「->」と型を省略する  
2.「->()」  
3.「-> Void」  
```
// 基本
func 関数名 (仮引数: 型) -> 型 {
    do anything
}
```
###### 引数ラベルの省略  
```
func area(_ h: Double, _ w:Double) -> Double{
    return h * w
}

// 呼び出し元
let a = area(10.0, 12.5)
```
###### 仮引数の省略
```
// 第3引数を関数で利用しない場合
func compare(_ a:Int, _ b:Int, _:Bool)

// 引数のラベルは指定したい場合
func compare(_ a:Int, _ b:Int, option _:Bool)

// 呼び出し元
compare(10, 8, option:true)
```

### 返り値を使わない場合の関数  
@discardableResult の属性を指定する  
```
@discardableResult
func sayHellor(to n:String) -> Bool{}
```

### tuple
配列やDictionaryのようにデータ型の違う複数の値を一時的に保持したいときに使う  
https://wp-p.info/tpl_rep.php?cat=swift-biginner&fl=r22  

### 型キャスト
・アップキャスト : 継承先のインスタンスの型を継承元のクラスとして扱うこと  
```
//as String型からAny型へアップキャスト
let str: String = "sample"
let any: Any = str as Any
```
・ダウンキャスト： 継承元のインスタンスの型を継承先のクラスとして扱うこと  
```
let any: Any = "sample" as Any
let str = any as? String
let int = any as? Int //→ nillになる
let int = any as! Int //→ 実行時エラー
```  




