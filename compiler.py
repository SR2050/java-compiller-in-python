import subprocess

java_code = '''
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
'''

# Save the Java code to a file
with open('HelloWorld.java', 'w') as file:
    file.write(java_code)

# Compile the Java code using the Java compiler
compile_process = subprocess.Popen(['javac', 'HelloWorld.java'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
compile_output, compile_error = compile_process.communicate()

if compile_process.returncode == 0:
    print("Compilation successful!")

    # Run the compiled Java program
    run_process = subprocess.Popen(['java', 'HelloWorld'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    run_output, run_error = run_process.communicate()

    if run_process.returncode == 0:
        print("Output:")
        print(run_output.decode('utf-8'))
    else:
        print("Runtime Error:")
        print(run_error.decode('utf-8'))
else:
    print("Compilation Error:")
    print(compile_error.decode('utf-8'))
