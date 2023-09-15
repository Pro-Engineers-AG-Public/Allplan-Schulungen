<?xml version="1.0" encoding="utf-8"?>
<Element>
    <Script>
        <Name>ProEngineers\Schulung\PythonPart.py</Name>
        <Title>Cable Cart</Title>
        <Version>0.0.1.0</Version>
        <Interactor>False</Interactor>
    </Script>
	<Page>
		<Name>Properties</Name>
		<Text></Text>
        <Parameter>
            <Name>Length</Name>
            <Text>Length of cube</Text>
            <Value>1000.0</Value>
            <ValueType>Length</ValueType>
        </Parameter>
        <Parameter>
            <Name>Width</Name>
            <Text>Width of cube</Text>
            <Value>1000.0</Value>
            <ValueType>Length</ValueType>
        </Parameter>
        <Parameter>
            <Name>Height</Name>
            <Text>Height of cube</Text>
            <Value>1000.0</Value>
            <ValueType>Length</ValueType>
        </Parameter>
        <Parameter>
            <Name>Expander</Name>
            <ValueType>Expander</ValueType>
            <Text>Translation</Text>
            <Visible>True</Visible>
            <Parameter>
                <Name>Translation</Name>
                <Text>Translation of cube</Text>
                <Value>Point3D(0,0,0)</Value>
                <ValueType>Point3D</ValueType>
            </Parameter>
        </Parameter>

        <Parameter>
            <Name>Expander</Name>
            <ValueType>Expander</ValueType>
            <Text>Rotation</Text>
            <Visible>True</Visible>
            <Parameter>
                <Name>RotationX</Name>
                <Text>X-Rotation of cube</Text>
                <Value>0</Value>
                <ValueType>Angle</ValueType>
            </Parameter>
            <Parameter>
                <Name>RotationY</Name>
                <Text>Y-Rotation of cube</Text>
                <Value>0</Value>
                <ValueType>Angle</ValueType>
            </Parameter>
            <Parameter>
                <Name>RotationZ</Name>
                <Text>Z-Rotation of cube</Text>
                <Value>0</Value>
                <ValueType>Angle</ValueType>
            </Parameter>
        </Parameter>
        
    </Page>
</Element>