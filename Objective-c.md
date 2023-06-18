
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
