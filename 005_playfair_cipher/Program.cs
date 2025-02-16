
using System;
using System.Text;
using System.Collections.Generic;

namespace ConsoleApp1
{
    class Program
    {
        public static void Playfair()
        {
            var alf = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ_.,";
            //var key = "РЕПАБВ";
            //var str = "РЕГИСТРАЦИЯ_СОБЫТИЙ";

            var key = "РЕДЬКА";
            var str = "ИЗКОЬПВКОЙЬЮГСИАВКОЙНЧ";

            var line = "";
            //Matrix(alf, key);
            Bigramms(str);
            line = EncryptionPlayfair(alf, key, str);
            Console.WriteLine(line);
            line = DecryptionPlayfair(alf, key, str);
            Console.WriteLine(line);

        }

        private static string EncryptionPlayfair(string alf, string key, string str)
        {
            var matrix = Matrix(alf, key);
            var bigramms = Bigramms(str);

            var bigrammCode = new List<string>();

            var corner = new[] { new int[] { 0, 0 }, new int[] { 0, 0 } };

            foreach (var bigram in bigramms)
            {
                for (int i = 0; i < matrix.GetLength(1); i++)
                    for (int j = 0; j < matrix.GetLength(0); j++)
                    {
                        if (matrix[i, j] == bigram[0])
                        {
                            corner[0][0] = i;
                            corner[0][1] = j;
                        }
                        if (matrix[i, j] == bigram[1])
                        {
                            corner[1][0] = i;
                            corner[1][1] = j;
                        }
                    }
                // По столбцам
                if (corner[0][1] == corner[1][1])
                {
                    corner[0][0]++;
                    corner[1][0]++;
                    if (corner[0][0] == matrix.GetLength(0))
                        corner[0][0] = 0;
                    if (corner[1][0] == matrix.GetLength(0))
                        corner[1][0] = 0;
                    bigrammCode.Add(matrix[corner[0][0], corner[0][1]].ToString() +
                                    matrix[corner[1][0], corner[1][1]].ToString());
                }
                else
                // По строкам
                if (corner[0][0] == corner[1][0])
                {
                    corner[0][1]++;
                    corner[1][1]++;
                    if (corner[0][1] == matrix.GetLength(1))
                        corner[0][1] = 0;
                    if (corner[1][1] == matrix.GetLength(1))
                        corner[1][1] = 0;
                    bigrammCode.Add(matrix[corner[0][0], corner[0][1]].ToString() +
                                    matrix[corner[1][0], corner[1][1]].ToString());
                }
                else
                // Прямоугольник
                {
                    /*
                     *      A       *   
                     * 
                     *      *       B
                     */
                    if (corner[0][0] < corner[1][0] && corner[0][1] < corner[1][1])
                    {
                        bigrammCode.Add(matrix[corner[0][0], corner[1][1]].ToString() +
                                        matrix[corner[1][0], corner[0][1]].ToString());
                    }

                    /*
                     *      *       A   
                     * 
                     *      B       *
                     */
                    if (corner[0][0] < corner[1][0] && corner[0][1] > corner[1][1])
                    {
                        bigrammCode.Add(matrix[corner[1][0], corner[0][1]].ToString() +
                                        matrix[corner[0][0], corner[1][1]].ToString());
                    }

                    /*
                     *      B       *   
                     * 
                     *      *       A
                     */
                    if (corner[1][0] < corner[0][0] && corner[1][1] < corner[0][1])
                    {
                        bigrammCode.Add(matrix[corner[0][0], corner[1][1]].ToString() +
                                        matrix[corner[1][0], corner[0][1]].ToString());
                    }

                    /*
                     *      *       B   
                     * 
                     *      A       *
                     */
                    if (corner[1][0] < corner[0][0] && corner[1][1] > corner[0][1])
                    {
                        bigrammCode.Add(matrix[corner[1][0], corner[0][1]].ToString() +
                                        matrix[corner[0][0], corner[1][1]].ToString());
                    }
                }
            }

            var result = new StringBuilder();
            foreach (var word in bigrammCode)
                result.Append(word.ToString());
            var line = result.ToString();
            return line; ;
        }

        private static string DecryptionPlayfair(string alf, string key, string str)
        {
            var matrix = Matrix(alf, key);
            var bigramms = Bigramms(str);

            var bigrammCode = new List<string>();

            var corner = new[] { new int[] { 0, 0 }, new int[] { 0, 0 } };

            foreach (var bigram in bigramms)
            {
                for (int i = 0; i < matrix.GetLength(1); i++)
                    for (int j = 0; j < matrix.GetLength(0); j++)
                    {
                        if (matrix[i, j] == bigram[0])
                        {
                            corner[0][0] = i;
                            corner[0][1] = j;
                        }
                        if (matrix[i, j] == bigram[1])
                        {
                            corner[1][0] = i;
                            corner[1][1] = j;
                        }
                    }
                // По столбцам
                if (corner[0][1] == corner[1][1])
                {
                    corner[0][0]--;
                    corner[1][0]--;
                    if (corner[1][0] == -1)
                        corner[1][0] = matrix.GetLength(0) - 1;
                    if (corner[0][0] == -1)
                        corner[0][0] = matrix.GetLength(0) - 1;
                    bigrammCode.Add(matrix[corner[0][0], corner[0][1]].ToString() +
                                    matrix[corner[1][0], corner[1][1]].ToString());
                }
                else
                // По строкам
                if (corner[0][0] == corner[1][0])
                {
                    corner[0][1]--;
                    corner[1][1]--;
                    if (corner[0][1] == -1)
                        corner[0][1] = matrix.GetLength(1) - 1;
                    if (corner[1][1] == -1)
                        corner[1][1] = matrix.GetLength(1) - 1;
                    bigrammCode.Add(matrix[corner[0][0], corner[0][1]].ToString() +
                                    matrix[corner[1][0], corner[1][1]].ToString());
                }
                else
                // Прямоугольник
                {
                    /*
                     *      A       *   
                     * 
                     *      *       B
                     */
                    if (corner[0][0] < corner[1][0] && corner[0][1] < corner[1][1])
                    {
                        bigrammCode.Add(matrix[corner[1][0], corner[0][1]].ToString() +
                                        matrix[corner[0][0], corner[1][1]].ToString());
                    }

                    /*
                     *      *       A   
                     * 
                     *      B       *
                     */
                    if (corner[0][0] < corner[1][0] && corner[0][1] > corner[1][1])
                    {
                        bigrammCode.Add(matrix[corner[0][0], corner[1][1]].ToString() +
                                        matrix[corner[1][0], corner[0][1]].ToString());
                    }

                    /*
                     *      B       *   
                     * 
                     *      *       A
                     */
                    if (corner[1][0] < corner[0][0] && corner[1][1] < corner[0][1])
                    {
                        bigrammCode.Add(matrix[corner[1][0], corner[0][1]].ToString() +
                                        matrix[corner[0][0], corner[1][1]].ToString());
                    }

                    /*
                     *      *       B   
                     * 
                     *      A       *
                     */
                    if (corner[1][0] < corner[0][0] && corner[1][1] > corner[0][1])
                    {
                        bigrammCode.Add(matrix[corner[0][0], corner[1][1]].ToString() +
                                        matrix[corner[1][0], corner[0][1]].ToString());
                    }
                }
            }


            var result = new StringBuilder();
            foreach (var word in bigrammCode)
                result.Append(word.ToString());
            var line = result.ToString();
            return line;
        }

        private static char[,] Matrix(string alf, string key)
        {
            var matrix = new char[6, 6];

            for (int j = 0; j < key.Length; j++)
                matrix[j / 6, j % 6] = key[j];

            int k = 0;
            for (int i = 0; i < 6; i++)
                for (int j = 0; j < 6; j++)
                {
                    if (matrix[i, j] == 0)
                    {
                        while (k < alf.Length)
                            if (!key.Contains(alf[k]))
                            {
                                matrix[i, j] = alf[k];
                                k++;
                                break;
                            }
                            else
                                k++;
                    }
                }

            for (int i = 0; i < 6; i++)
            {
                for (int j = 0; j < 6; j++)
                    Console.Write(matrix[i, j].ToString() + ' ');
                Console.WriteLine();
            }
            return matrix;
        }

        private static string[] Bigramms(string str)
        {
            var bidrammsList = new List<string>();

            int i = 0;
            while (true)
            {
                if (i < str.Length)
                {
                    if (i + 1 == str.Length || str[i] == str[i + 1])
                    {
                        bidrammsList.Add(str[i].ToString() + 'Ъ');
                        i++;
                        continue;
                    }
                    else
                    {
                        bidrammsList.Add(str.Substring(i, 2));
                        i += 2;
                        continue;
                    }
                }
                else
                    break;
            }
            return bidrammsList.ToArray();
        }

        public static void Main()
        {
            Playfair();
            Console.ReadKey();
        }
    }
}