find
	void CAniImageBox::SetScale(float fx, float fy)

add(or just add anywhere..)

	void CAniImageBox::SetRotation(float fRotation)
	{
		for (const auto& memberImg : m_ImageVector)
			memberImg->SetRotation(fRotation);
	}