using System;
using System.Timers;

class Program
{
    private static Timer aTimer;

    static void Main()
    {
        aTimer = new Timer(1000);
        aTimer.Elapsed += OnTimedEvent;
        aTimer.AutoReset = true;
        aTimer.Enabled = true;
        Console.WriteLine("Presiona la tecla 'q' para salir del programa...");
        while(Console.Read() != 'q');
    }

    private static void OnTimedEvent(Object source, ElapsedEventArgs e)
    {
        Console.Clear();
        Console.WriteLine("La hora es: {0:HH:mm:ss}", e.SignalTime);
    }
}