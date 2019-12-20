

#include <iostream>
#include <Windows.h> // Used for defining Sleep Function

using namespace std;

int switchCase = 1;

/*Class definition*/
class machineState
{

public:

	void machineIdleState();
	void machineSensingState();
	void machineProcessingState();
};

/*Enumeration definitions*/
enum switchCases
{
	idleState = 1,
	sensingState = 2,
	processingState = 3,
};


/*Sensing State Function Definition*/
void machineState::machineSensingState()
{
	cout << "Machine State Changed : Sensing >> Processing" << endl;
	Sleep(5000);
	switchCase = processingState;
}

/*Processing State Function Definition*/
void machineState::machineProcessingState()
{

	
	cout << "Machine State Changed : Processing  >> Idle" << endl;
	Sleep(5000);
	switchCase = idleState;
}

/*Idle State Function Definition*/
void machineState::machineIdleState()
{

	cout <<"Machine State Changed : Idle >> Sensing" << endl;
	Sleep(5000);
	switchCase = sensingState;
}


/* Main Function Definition */
int main()
{
	machineState object;
	while (1)
	{
		switch (switchCase)
		{
		case 1:
			object.machineIdleState();
			break;
		case 2:
			object.machineSensingState();
			break;
		case 3:
			object.machineProcessingState();
			break;
		}
	}

}

