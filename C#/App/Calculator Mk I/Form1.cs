namespace Calculator_Mk_I
{
    public partial class Form1 : Form
    {
        string numberfirst;
        //string numbersecond;
        int firststring;

        public Form1()
        {
            InitializeComponent();
            label1.Text = "0";
            while (true)
            {
               firststring = Convert.ToInt32(numberfirst);
                Console.ReadKey();
            }
        }


        private void button1_Click(object sender, EventArgs e)
        {
            numberfirst += "1";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            numberfirst += "2";
        }
        private void button3_Click(object sender, EventArgs e)
        {
            numberfirst += "3";
        }
        private void button4_Click(object sender, EventArgs e)
        {
            numberfirst += "4";
        }
        private void button5_Click(object sender, EventArgs e)
        {
            numberfirst += "5";
        }
        private void button6_Click(object sender, EventArgs e)
        {
            numberfirst += "6";
        }
        private void button7_Click(object sender, EventArgs e)
        {
            numberfirst += "7";
        }
        private void button8_Click(object sender, EventArgs e)
        {
            numberfirst += "8";
        }
        private void button9_Click(object sender, EventArgs e)
        {
            numberfirst += "9";
        }
        private void button10_Click(object sender, EventArgs e)
        {
            numberfirst += "10";
        }
        private void button11_Click(object sender, EventArgs e)
        {
            numberfirst += "0";
        }
        private void button12_Click(object sender, EventArgs e)
        {
            numberfirst += ".";
        }

        private void button13_Click(object sender, EventArgs e)
        {
        }

        private void label1_Click(object sender, EventArgs e)
        {
        }
    }
}
