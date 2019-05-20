import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Arrays;

import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import com.google.gson.Gson;

import java.io.Writer;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.FileOutputStream;
import java.io.IOException;

class ResultsSummary {
    List<String> headers;
    List<String> descriptions;
}

public class JSONRunner {
    public static void main(String[] args) {
        JUnitCore jc = new JUnitCore();
        System.out.println(args[0]);
        Class<?> wheatClass = SomeClassTester.class;

        Result result = jc.run(wheatClass);
        List<Failure> wheatFails = result.getFailures();

        Map<String,String> failures = new HashMap<>();

        for (Failure f: wheatFails) {
            String msg = f.getMessage();
            if (msg == null) {
                msg = f.getException().toString() + "\n" + Arrays.toString(f.getException().getStackTrace());
            }
            else {
                msg += "\n" + f.getException().toString() + Arrays.toString(f.getException().getStackTrace());
            }
            failures.put(f.getTestHeader(), msg);
        }

        Gson gs = new Gson();
        String output = gs.toJson(failures);

        Writer writer = null;

        try {
            writer = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(args[0]), "utf-8"));
            writer.write(output);
        } catch (IOException ex) {
        // report
        } finally {
            try {writer.close();} catch (Exception ex) {/*ignore*/}
        }			
    }
}
