using Multithreading;

class Program
{
    static void Main(string[] args)
    {

        #region threadpool
        //Console.WriteLine("Main thread started.");

        //// Queue a task to the ThreadPool
        //for (int i = 0; i < 5; i++)
        //{
        //    ThreadPool.QueueUserWorkItem(new WaitCallback(DoWork), i);
        //}

        //Console.WriteLine("Main thread doing other work...");

        //// Sleep to allow time for threads to complete before the application exits
        //Thread.Sleep(3000);

        //Console.WriteLine("Main thread ended.");
        #endregion


        LockFreeCounter counter = new LockFreeCounter();
        int taskCount = 10000;

        // Run tasks in parallel to increment the counter
        Parallel.For(0, taskCount, i =>
        {
            counter.Increment(); // Each task increments the counter
        });

        Console.WriteLine($"Final counter value: {counter.GetCount()}");

        // Ensure that all increments happened correctly
        if (counter.GetCount() == taskCount)
        {
            Console.WriteLine("All increments were successful.");
        }
        else
        {
            Console.WriteLine("Something went wrong.");
        }

    }



    // Method to perform work on a thread pool thread
    static void DoWork(object state)
    {
        int taskNumber = (int)state;
        Console.WriteLine($"Task {taskNumber} started on thread {Thread.CurrentThread.ManagedThreadId}");

        // Simulate work
        Thread.Sleep(1000);

        Console.WriteLine($"Task {taskNumber} completed on thread {Thread.CurrentThread.ManagedThreadId}");
    }
}
