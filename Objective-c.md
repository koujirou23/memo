
#### Webviewのインスタンス
```
#import <WebKit/WebKit.h>

WKWebView *webView = [[WKWebView alloc] initWithFrame:CGRectMake(0, 0, 320, 480)];
```


#### JSONデータの作成
```
NSDictionary *jsonData = @{@"key1": @"value1", @"key2": @"value2"};

NSError *error;
NSData *jsonPayload = [NSJSONSerialization dataWithJSONObject:jsonData options:0 error:&error];
```

#### リクエストを作成してJSONデータを設定
```
NSMutableURLRequest *request = [NSMutableURLRequest requestWithURL:[NSURL URLWithString:@"http://example.com/submit"]];
request.HTTPMethod = @"POST";
[request setValue:@"application/json" forHTTPHeaderField:@"Content-Type"];
[request setHTTPBody:jsonPayload];
```

#### リクエストをロード
```
[webView loadRequest:request];
```

## HTTP Header 
#### HTTPヘッダー追加
setValue:forHTTPHeaderField:メソッドは2つのパラメータを受け取ります。1つ目のパラメータvalueは、設定するヘッダーの値（Value）を表します。  
2つ目のパラメータfieldは、設定するヘッダーの名前（Field）を表します。  
以下は、setValue:forHTTPHeaderField:メソッドを使用してヘッダーを設定する例です
```
NSMutableURLRequest *request = [NSMutableURLRequest requestWithURL:[NSURL URLWithString:@"http://example.com"]];
[request setValue:@"application/json" forHTTPHeaderField:@"Content-Type"];

```
この例では、setValue:forHTTPHeaderField:メソッドを使用して、"Content-Type"という名前のヘッダーに"application/json"という値を設定しています。  
これにより、リクエストにJSONデータを含んでいることを示すためのヘッダーが設定されます。

## 表示するページのフォームにデータを入力
WKWebViewを使用してJSONデータをPOSTし、表示先のページのフォームに値を入力するには、  
JavaScriptを使用して以下の手順を実行します。  
WKWebViewのevaluateJavaScript:completionHandler:メソッドを使用してJavaScriptコードを実行します。  
このJavaScriptコードは、表示先のページのフォームに値を設定するために使用されます  
```
NSString *input1Value = @"Value 1";
NSString *input2Value = @"Value 2";

NSString *javaScriptCode = [NSString stringWithFormat:@"document.getElementById('input1').value = '%@'; document.getElementById('input2').value = '%@';", input1Value, input2Value];

[webView evaluateJavaScript:javaScriptCode completionHandler:^(id _Nullable result, NSError * _Nullable error) {
    // JavaScriptの実行が完了した後に実行される処理
    if (error) {
        NSLog(@"JavaScript Error: %@", error);
    } else {
        NSLog(@"JavaScript executed successfully");
    }
}];
```
上記の例では、input1とinput2というIDを持つフォーム要素に対して、input1Valueとinput2Valueの値を設定しています。  
javaScriptCodeには、フォームに値を設定するためのJavaScriptコードが格納されています。  
  
evaluateJavaScript:completionHandler:メソッドを呼び出し、WKWebViewでJavaScriptコードを実行します。  
コンプリーションハンドラー内で、JavaScriptの実行が成功したかどうかを確認できます。  
  
注意点として、JavaScriptを使用してフォームに値を設定するためには、表示先のページに対して操作が可能である必要があります。  
また、フォーム要素のIDやセレクタが正確であることを確認してください。  
  
以上の手順を実行することで、Objective-CのWKWebViewを使用してJSONデータをPOSTし、  
表示先のページのフォームに値を入力することができます。

## まとめ
```
#import <WebKit/WebKit.h>

// WKWebViewのインスタンス生成
WKWebView *webView = [[WKWebView alloc] initWithFrame:CGRectMake(0, 0, 320, 480)];

// JSONデータの生成
NSDictionary *jsonData = @{@"key1": @"value1", @"key2": @"value2"};
NSError *error;
NSData *jsonPayload = [NSJSONSerialization dataWithJSONObject:jsonData options:0 error:&error];

// WKWebViewのリクエストを生成
NSMutableURLRequest *request = [NSMutableURLRequest requestWithURL:[NSURL URLWithString:@"http://example.com/submit"]];
request.HTTPMethod = @"POST";
[request setValue:@"application/json" forHTTPHeaderField:@"Content-Type"];
[request setHTTPBody:jsonPayload];


// リクエストをロード
[webView loadRequest:request];


// 表示先のフォームに値を入力するJavaScript
NSString *input1Value = @"Value 1";
NSString *input2Value = @"Value 2";

// input1とinput2というIDを持つフォーム要素に対して、値を設定
NSString *javaScriptCode = [NSString stringWithFormat:@"document.getElementById('input1').value = '%@'; document.getElementById('input2').value = '%@';", input1Value, input2Value];

[webView evaluateJavaScript:javaScriptCode completionHandler:^(id _Nullable result, NSError * _Nullable error) {
    // JavaScriptの実行が完了した後に実行される処理
    if (error) {
        NSLog(@"JavaScript Error: %@", error);
    } else {
        NSLog(@"JavaScript executed successfully");
    }
}];
```



