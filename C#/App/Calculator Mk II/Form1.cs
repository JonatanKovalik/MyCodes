using System.Diagnostics;

namespace Calculator_Mk_II
{
    public partial class Form1 : Form
    {
        string firststring = "";
        int numberintfirst;
        public Form1()
        {
            InitializeComponent();
            main();
        }
        void main()
        {
            while (true)
            {
                NumbersText.Text = firststring;
                Thread.Sleep(1000);
            }
        }
        private void button1_Click(object sender, EventArgs e)
        {
            firststring += "1";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            firststring += "2";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            firststring += "3";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            firststring += "4";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            firststring += "5";
        }

        private void button6_Click(object sender, EventArgs e)
        {
            firststring += "6";
        }

        private void button7_Click(object sender, EventArgs e)
        {
            firststring += "7";
        }

        private void button8_Click(object sender, EventArgs e)
        {
            firststring += "8";
        }

        private void button9_Click(object sender, EventArgs e)
        {
            firststring += "9";
        }

        private void button10_Click(object sender, EventArgs e)
        {
            firststring += "0";
        }

        private void button11_Click(object sender, EventArgs e)
        {
            firststring += ".";
        }

        private void button12_Click(object sender, EventArgs e)
        {
           //numberintfirst = Convert.ToInt32(firststring);
        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
