using System.Collections;
using System.Collections.Generic;
using System;
using UnityEngine;
using System.Text;
using System.Threading.Tasks;
using System.Net.WebSockets;
using System.Threading;
using Newtonsoft.Json;

public class rSageCmd
{
    public MerakiDeviceDictionary cmd;
}

public class MerakiDevice {
    public string serial;
    public float lat;
    public float lng;
}

public class MerakiDeviceDictionary
{
    public Dictionary<string,MerakiDevice> devices;
    //IEnumerable<IDictionary<string, MerakiDevice>> devices { get; set; }
}

public class BlockGenerator : MonoBehaviour {

    static ClientWebSocket webSocket = null;

    // Use this for initialization
    void Start () {
        string uri = @"ws://localhost:8080/unity";
        //Thread.Sleep(1000);
        //Connect(uri).Wait();
        Connect(uri);
    }
	
	// Update is called once per frame
	void Update () {
		// Process inbound commands
	}

    async void OnApplicationQuit()
    {
        //appIsRunning = false;
        Debug.Log("Application ending after " + Time.time + " seconds");
        await webSocket.CloseAsync(WebSocketCloseStatus.NormalClosure, "ClosedByApp", CancellationToken.None);
    }

    private static object consoleLock = new object();
    private const int sendChunkSize = 256;
    private const int receiveChunkSize = 256;
    private const bool verbose = true;
    //private static bool appIsRunning = true;
    private static readonly TimeSpan delay = TimeSpan.FromMilliseconds(3000);

    public static async Task Connect(string uri)
    {

        try
        {
            webSocket = new ClientWebSocket();
            await webSocket.ConnectAsync(new Uri(uri), CancellationToken.None);
            await Task.WhenAll(Receive(webSocket), Send(webSocket));
            byte[] buffer = encoder.GetBytes("Task completed!");
            LogStatus(false, buffer, buffer.Length);
        }
        catch (Exception ex)
        {
            Console.WriteLine("Exception: {0}", ex);
        }
        finally
        {
            if (webSocket != null)
                webSocket.Dispose();
            Console.WriteLine();

            lock (consoleLock)
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("WebSocket closed.");
                Console.ResetColor();
            }
        }
    }
    static UTF8Encoding encoder = new UTF8Encoding();

    private static async Task Send(ClientWebSocket webSocket)
    {

        //byte[] buffer = encoder.GetBytes("{\"op\":\"blocks_sub\"}"); //"{\"op\":\"unconfirmed_sub\"}");
        //byte[] buffer = encoder.GetBytes(@"{""cmd"":""HELLO""}");
        byte[] buffer = encoder.GetBytes(@"{""cmd"":""appCmdWithToken"",""data"":{""appName"":""HiveAccess"",""appCmd"":""getMerakiAPs"",""appData"":""fakestats""}}");
        await webSocket.SendAsync(new ArraySegment<byte>(buffer), WebSocketMessageType.Text, true, CancellationToken.None);
        /*
        while (webSocket.State == WebSocketState.Open)
        {
            LogStatus(false, buffer, buffer.Length);
            await Task.Delay(delay);
        }
        */
    }

    private static async Task Receive(ClientWebSocket webSocket)
    {
        //ArraySegment<Byte> buffer = new ArraySegment<byte>(new Byte[8192]);
        int BufferSize = 8192;
        var temporaryBuffer = new byte[BufferSize];
        var buffer = new byte[BufferSize * 20];
        int offset = 0;

        //byte[] buffer = new byte[receiveChunkSize];
        while (webSocket.State == WebSocketState.Open)

        {
            while (true)
            {
                var response = await webSocket.ReceiveAsync(
                                     new ArraySegment<byte>(temporaryBuffer),
                                     CancellationToken.None);
                temporaryBuffer.CopyTo(buffer, offset);
                offset += response.Count;
                temporaryBuffer = new byte[BufferSize];
                if (response.EndOfMessage)
                {
                    //GameObject cube = GameObject.CreatePrimitive(PrimitiveType.Cube);
                    //cube.transform.position = new Vector3(0, 0.5F, 0);
                    //Console.WriteLine(buffer);
                    var bytesAsString = Encoding.UTF8.GetString(buffer);
                    print(bytesAsString);

                    rSageCmd personDictionaryCmd = JsonConvert.DeserializeObject<rSageCmd>(bytesAsString);

                    var test = 1;

                    foreach (var keyvalue in personDictionaryCmd.cmd.devices)
                    {
                        MerakiDevice thisDevice = keyvalue.Value;
                        //var thisDevice = personDictionaryCmd.cmd.devices[];
                        //textBox.text = keyvalue.Value; // this will only display the value of that
                        // attribute / key 
                        GameObject cube = GameObject.CreatePrimitive(PrimitiveType.Cube);
                        //cube.transform.transform.localScale += new Vector3(.5f, .5f, .5f);
                        cube.transform.position = new Vector3(0.25f, 0.25f, 0.25f);
                        cube.transform.position = new Vector3(thisDevice.lat/10, 0.25f, thisDevice.lng / 10);

                        Material newMat = Resources.Load("red", typeof(Material)) as Material;
                        cube.GetComponent<Renderer>().material.color = Color.red;
                    }

                    buffer = new byte[BufferSize * 20];
                    offset = 0;

                    break;
                }
            }
            /*
            Array.Clear(buffer, 0, buffer.Length);
            var result = await webSocket.ReceiveAsync(new ArraySegment<byte>(buffer), CancellationToken.None);
            if (result.MessageType == WebSocketMessageType.Close)
            {
                await webSocket.CloseAsync(WebSocketCloseStatus.NormalClosure, string.Empty, CancellationToken.None);
            }
            else
            {
                LogStatus(true, buffer, result.Count);

                GameObject cube = GameObject.CreatePrimitive(PrimitiveType.Cube);
                cube.transform.position = new Vector3(0, 0.5F, 0);
            }
            */
        }
    }

    private static void LogStatus(bool receiving, byte[] buffer, int length)
    {
        lock (consoleLock)
        {
            Console.ForegroundColor = receiving ? ConsoleColor.Green : ConsoleColor.Gray;
            Console.WriteLine("{0} ", receiving ? "Received" : "Sent");

            if (verbose)
                Console.WriteLine(encoder.GetString(buffer));

            Console.ResetColor();
        }
    }
}
