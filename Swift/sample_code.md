
```
let str: String = self.dict().object(forKey: "apple") as! String

let str: String = (self.dict().object(forKey: "apple") as! String).uppercased()

```

```
let str: String = (dict(str: "100").object(forKey: "apple") as! String).uppercased()
print(str)
```
```
func dict(str: String) -> NSDictionary {
    if str == "100"{
        let dict2: NSDictionary = ["apple": "5", "banana": "6"]
        return dict2
    }
    return [:]
}

```