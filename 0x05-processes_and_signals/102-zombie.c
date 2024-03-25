#include <unistd.h>


/**
 * infinite_while - sleeping func
 * Return: nothing
*/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Entry point
 * Return: 0 on success
*/
int main(void)
{
	int x;
	int i = 0;

	while (i < 5)
	{
		x = fork();
		if (x == 0)
		{
			return (0);
		}
		else
		{
			++i;
			infinite_while();
		}
	}
	return (0);
}
