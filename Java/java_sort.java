import org.json.JSONArray;
import org.json.JSONObject;
import org.json.JSONTokener;

import java.io.FileReader;

public class JsonSorter {
    public static void main(String[] args) throws Exception {
        // JSONファイルを読み込む
        FileReader fileReader1 = new FileReader("file1.json");
        FileReader fileReader2 = new FileReader("file2.json");

        // JSONファイルをJavaオブジェクトに変換する
        JSONTokener tokener1 = new JSONTokener(fileReader1);
        JSONTokener tokener2 = new JSONTokener(fileReader2);

        JSONObject jsonObject1 = new JSONObject(tokener1);
        JSONObject jsonObject2 = new JSONObject(tokener2);

        // Javaオブジェクトをソートする
        JSONArray jsonArray1 = jsonObject1.getJSONArray("array");
        JSONArray jsonArray2 = jsonObject2.getJSONArray("array");

        jsonArray1.sort((o1, o2) -> ((JSONObject) o1).getInt("id") - ((JSONObject) o2).getInt("id"));
        jsonArray2.sort((o1, o2) -> ((JSONObject) o1).getInt("id") - ((JSONObject) o2).getInt("id"));

        // ソートされたJavaオブジェクトをJSONファイルに変換する
        jsonObject1.put("array", jsonArray1);
        jsonObject2.put("array", jsonArray2);

        System.out.println(jsonObject1.toString(4));
        System.out.println(jsonObject2.toString(4));
    }
}
