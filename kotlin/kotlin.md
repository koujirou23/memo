## Kotlin メモ
#### 条件判定 when 式
javaで言うところのSwtich文  
```
val value = 1
val str = when(value) {
  value == 1 -> "one"
  value == 2 -> "two"
  else -> "other"
}

val value = 1
val str = when(value) {
  1 -> "one"
  2 -> "two"
  else -> "other"
}
```

#### ループ
```
val array: Array<Int> = arrayOf(1,2,3,4,5)
for(i in array){
  print(i) // → 12345
}

for(i in 0..4){
  print(i) // →01234
}

//逆順のループ
for(i in 4 downTo 0){
  print(i) // →43210
}

var i = 0
while (i < 10) {
  print(i++) // → 0123456789
}

var i = 0
do {
  print(i++) // → 0123456789
} while(i < 10)
```

#### Kotlin 関数
arrayOf:配列を制しえする関数  
listOf:リストを生成する関数  
mapOf:マップを生成する関数  
setOf:セットを生成する関数  
